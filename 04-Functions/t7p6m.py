def hide(card_number):
    hidden_card_number = ""
    card_number = str(card_number)
    if not len(card_number) == 16:
        return "Wrong length"
    else:
        hidden_card_number = card_number[:2] + "**********" + card_number[12:]
        return hidden_card_number
    
if __name__ == "__main__":
    print(hide(5290312400019022))