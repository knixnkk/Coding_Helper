def number_to_words(num):
    if num == 0:
        return "Zero"

    def one_to_nineteen(n):
        return ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                "Seventeen", "Eighteen", "Nineteen"][n]

    def tens(n):
        return ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"][n]

    def below_thousand(n):
        if n == 0:
            return ""
        elif n < 20:
            return one_to_nineteen(n)
        elif n < 100:
            return tens(n // 10) + (" " + one_to_nineteen(n % 10) if n % 10 != 0 else "")
        else:
            return one_to_nineteen(n // 100) + " Hundred" + (" " + below_thousand(n % 100) if n % 100 != 0 else "")

    def large_number_words(n):
        levels = ["", "Thousand", "Million", "Billion", "Trillion"]
        parts = []
        level = 0
        while n > 0:
            if n % 1000 != 0:
                parts.append(below_thousand(n % 1000) + " " + levels[level])
            n //= 1000
            level += 1
        return " ".join(reversed([p.strip() for p in parts if p]))

    return large_number_words(num).strip()

n = int(input("Enter a number: "))
print(number_to_words(n)) 

