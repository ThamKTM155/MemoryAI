"""
Knowledge Builder
BUILD-35.1

Nhiệm vụ:
- Chuyển Summary Metadata thành Knowledge Record.
- Không đọc file.
- Không ghi file.
- Không Validation.
- Không tạo Relationships.
"""


def build_knowledge(metadata):
    """
    Build Knowledge Record từ Summary Metadata.

    Parameters
    ----------
    metadata : dict

    Returns
    -------
    dict
        Knowledge Record.
    """

    knowledge = {
        "id": metadata.get("id", ""),
        "date": metadata.get("date", ""),
        "source": metadata.get("source", ""),
        "version": metadata.get("version", ""),

        "keywords": list(metadata.get("keywords", [])),
        "projects": list(metadata.get("projects", [])),

        # Các trường sẽ được BUILD sau bổ sung
        "decisions": [],
        "lessons": [],
        "tasks": []
    }

    return knowledge