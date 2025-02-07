class Solution(object):
    def simplifyPath(self, path):
        path_stack = []
        current_directory = ""

        for i, ch in enumerate(path):
            if ch == "/":
                if current_directory == ".." and path_stack:
                    path_stack.pop()
                    current_directory = ""
                elif current_directory not in [".", "", ".."]:
                    path_stack.append(current_directory)
                    current_directory = ""
                elif current_directory in [".", ".."]:
                    current_directory = ""

            if ch != "/":
                current_directory += ch

            if i == len(path)-1:
                if current_directory == ".." and path_stack:
                    path_stack.pop()
                elif current_directory not in [".", "", ".."]:
                    path_stack.append(current_directory)

        result = "/" + "/".join(path_stack)

        return result
