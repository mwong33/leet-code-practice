class Solution:
    # O(nlogn + m * n * m) time O(m) space
    # n - length of products
    # m - length of searchWord
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort products
        # loop through each character in searchWord to get a query (append to an overall query we generate)
        # check each word in our repo to see if it starts with our query
        # if it matches add it to our matchlist
        # add our matchlist to our output
        query = ""
        output_list = []
        products.sort()
        
        for character in searchWord:
            query += character
            match_list = []
            for product in products:
                if product.startswith(query):
                    match_list.append(product)
                    
                if len(match_list) == 3:
                    break
                    
            output_list.append(match_list)
        return output_list
