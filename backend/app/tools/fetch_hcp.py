from sqlalchemy.orm import Session
from app.models.hcp import HCP

def fetch_hcp_tool(db: Session, payload: dict):
    hcp_id = payload.get("hcp_id")
    if not hcp_id:
        return {"error": "hcp_id is required"}

    hcp = db.query(HCP).filter(HCP.id == hcp_id).first()
    if not hcp:
        return {"error": "HCP not found"}

    return {
        "tool": "fetch_hcp_profile",
        "hcp": {
            "id": hcp.id,
            "name": hcp.name,
            "specialty": hcp.specialty,
            "hospital": hcp.hospital,
            "city": hcp.city
        }
    }