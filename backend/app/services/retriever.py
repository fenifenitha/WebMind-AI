class Retriever:

    def get_context(
        self,
        results
    ):

        contexts = []

        for item in results:

            contexts.append(
                item.payload["text"]
            )

        return "\n".join(contexts)
class Retriever:

    def get_context(self, results):

        contexts = []

        for item in results:

            if "text" in item.payload:
                contexts.append(
                    item.payload["text"]
                )

        return "\n".join(contexts)