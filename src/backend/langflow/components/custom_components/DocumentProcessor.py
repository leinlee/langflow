from langflow import CustomComponent
from langchain.schema import Document


class DocumentProcessor(CustomComponent):
    display_name = "My Processor"
    description = "This component processes a document"

    def build_config(self) -> dict:
        options = ["Uppercase", "Lowercase", "Titlecase"]
        return {
            "function": {
                "options": options,
                "value": options[0],
                "display_name": "Function",
            },
            "document": {"display_name": "Document"},
        }

    def build(self, document: Document, function: str) -> Document:
        if isinstance(document, list):
            document = document[0]
        page_content = document.page_content
        if function == "Uppercase":
            page_content = page_content.upper()
        elif function == "Lowercase":
            page_content = page_content.lower()
        elif function == "Titlecase":
            page_content = page_content.title()
        self.repr_value = f"Result of {function} function: {page_content}"
        return Document(page_content=page_content)
