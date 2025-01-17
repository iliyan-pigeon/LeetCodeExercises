class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = [""]
        row_counter = 0

        for index, word in enumerate(words):
            if len(result[row_counter]) + len(word) + 1 <= maxWidth:
                if result[row_counter] == "":
                    result[row_counter] += word
                else:
                    result[row_counter] += " "
                    result[row_counter] += word
            elif len(result[row_counter]) < maxWidth:
                if len(word) == maxWidth and result[-1] == "":
                    result[row_counter] += word
                    result.append("")
                    row_counter += 1
                    continue
                distributor = result[row_counter].split(" ")
                if len(distributor) == 1:
                    distributor[0] += " " * (maxWidth - len(distributor[0]))
                else:
                    counter = 0
                    for i in range(maxWidth - len(result[row_counter])):
                        if counter == len(distributor) - 1:
                            counter = 0

                        distributor[counter] += " "
                        counter += 1

                result[row_counter] = " ".join(distributor)
                result.append("")
                row_counter += 1
                result[row_counter] += word
            else:
                result.append("")
                row_counter += 1
                result[row_counter] += word

        if len(result[-1]) < maxWidth:
            result[-1] += " " * (maxWidth - len(result[-1]))

        if result[-1] == " ":
            result.remove(" ")

        return result
