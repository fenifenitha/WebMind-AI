from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

    def create_chunks(self, text):

        chunks = self.splitter.split_text(text)

        return chunks