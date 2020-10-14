ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion'}


def convert_number(i):
    if i < 0:
        return join_number('negative', number_pos(-i))
    if i == 0:
        return 'zero'
    return number_pos(i)


def number_pos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return join_number(tens[i // 10], ones[i % 10])
    if i < 1000:
        return divide(i, 100, 'hundred')
    for number, name in illions.items():
        if i < 1000 ** (number + 1):
            break
    return divide(i, 1000 ** number, name)


def divide(divid, divis, magnitude):
    return join_number(
        number_pos(divid // divis),
        magnitude,
        number_pos(divid % divis),
    )


def join_number(*args):
    return ' '.join(args)


print(convert_number(-23456767))
