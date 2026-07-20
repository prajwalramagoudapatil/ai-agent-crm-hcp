import re

from sqlalchemy.orm import Session

from app.models.hcp import HCP


def normalize_name(name: str | None) -> str:
    """
    Normalize doctor names before comparison.

    Examples:
        "Dr. Sharma"          -> "sharma"
        "DR SHARMA"           -> "sharma"
        " Dr.  Ravi Sharma "  -> "ravi sharma"
    """
    if not name:
        return ""

    name = name.lower().strip()

    # remove dr / dr.
    name = re.sub(r"\bdr\.?\b", "", name)

    # remove punctuation
    name = re.sub(r"[^\w\s]", "", name)

    # remove extra spaces
    name = " ".join(name.split())

    return name


def resolve_hcp(
    db: Session,
    selected_hcp_id: int | None,
    extracted_name: str | None,
):
    """
    Resolves whether the HCP selected in the UI matches
    the HCP mentioned in the chat.

    Returns:
        {
            "status": "...",
            "resolved_hcp_id": int | None,
            "selected_hcp_name": str | None,
            "mentioned_hcp_name": str | None
        }
    """
    print(" Resolving hcp")
    # -----------------------------
    # No HCP selected in UI
    # -----------------------------
    if selected_hcp_id is None:
        return {
            "status": "no_selected_hcp",
            "resolved_hcp_id": None,
            "selected_hcp_name": None,
            "mentioned_hcp_name": extracted_name,
        }

    # -----------------------------
    # Fetch selected HCP
    # -----------------------------
    selected_hcp = (
        db.query(HCP)
        .filter(HCP.id == selected_hcp_id)
        .first()
    )

    if selected_hcp is None:
        return {
            "status": "invalid_selected_hcp",
            "resolved_hcp_id": None,
            "selected_hcp_name": None,
            "mentioned_hcp_name": extracted_name,
        }

    # -----------------------------
    # No doctor mentioned in chat
    # -----------------------------
    if not extracted_name:
        return {
            "status": "selected_only",
            "resolved_hcp_id": selected_hcp.id,
            "selected_hcp_name": selected_hcp.doctor_name,
            "mentioned_hcp_name": None,
        }

    # -----------------------------
    # Compare names
    # -----------------------------
    selected_normalized = normalize_name(
        selected_hcp.doctor_name
    )

    extracted_normalized = normalize_name(
        extracted_name
    )

    if selected_normalized == extracted_normalized:
        return {
            "status": "match",
            "resolved_hcp_id": selected_hcp.id,
            "selected_hcp_name": selected_hcp.doctor_name,
            "mentioned_hcp_name": extracted_name,
        }

    # -----------------------------
    # Conflict
    # -----------------------------
    return {
        "status": "conflict",
        "resolved_hcp_id": selected_hcp.id,
        "selected_hcp_name": selected_hcp.doctor_name,
        "mentioned_hcp_name": extracted_name,
    }