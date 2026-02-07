import math
def mid(length):
    """
    Purpose:
        Return the middle index for a sequence of a given length.

    Parameters:
        length (int): Length of the sequence (>= 0).

    Returns:
        int: Middle index computed as floor((0 + (length-1)) / 2).
    """
    start = 0
    end = length - 1
    return (start + end) // 2


def median(x):
    """
    Purpose:
        Compute and return the median of an iterable of numeric values.

    Parameters:
        x (iterable): Iterable of numeric elements.

    Returns:
        float or int:
            - If length is odd: the middle value of the sorted data.
            - If length is even: the average of the two middle values.
    """
    x_sorted = sorted(x)
    n = len(x_sorted)
    if n == 0:
        raise ValueError("median() requires at least one value")

    m = n // 2
    if n % 2 == 1:
        return x_sorted[m]
    else:
        return (x_sorted[m - 1] + x_sorted[m]) / 2


def iqr(x):
    """
    Purpose:
        Compute and return the interquartile range (IQR) of an iterable x.

    Parameters:
        x (iterable): Iterable of numeric elements.

    Returns:
        float: IQR = Q3 - Q1, where:
            - If length is even (2n): Q1 is median of smallest n, Q3 median of largest n
            - If length is odd (2n+1): Q1 is median of smallest n+1, Q3 median of largest n+1
            - If length <= 1: IQR is 0.0
    """
    x_sorted = sorted(x)
    n = len(x_sorted)

    if n <= 1:
        return 0.0

    m = mid(n) 

    if n % 2 == 0:
        lower = x_sorted[:m + 1]   
        upper = x_sorted[m + 1:]
    else:
        lower = x_sorted[:m + 1]
        upper = x_sorted[m:]

    return float(median(upper) - median(lower))


def sixnum(x):
    """
    Purpose:
        Compute Tukey’s six-number summary for an iterable x:
        [min, Q1, median, average, Q3, max]

    Parameters:
        x (iterable): Iterable of numeric elements.

    Returns:
        list:
            [minimum, Q1, median, average (rounded to 2 decimals), Q3, maximum]
    """
    x_sorted = sorted(x)
    n = len(x_sorted)
    if n == 0:
        raise ValueError("sixnum() requires at least one value")

    mn = x_sorted[0]
    mx = x_sorted[-1]
    med = median(x_sorted)

    avg = round(sum(x_sorted) / n, 2)

    m = mid(n)
    if n % 2 == 0:
        lower = x_sorted[:m + 1]
        upper = x_sorted[m + 1:]
    else:
        lower = x_sorted[:m + 1]
        upper = x_sorted[m:]

    q1 = median(lower)
    q3 = median(upper)

    return [mn, q1, med, avg, q3, mx]


def order(x):
    """
    Purpose:
        Return indices of elements of x sorted from greatest to smallest.
        Ties keep original order (stable).

    Parameters:
        x (iterable): Iterable of numeric elements.

    Returns:
        list[int]: Indices sorted by descending value, stable on ties.
    """
    indexed = list(enumerate(x)) 
    indexed_sorted = sorted(indexed, key=lambda t: (-t[1], t[0]))
    return [idx for idx, _ in indexed_sorted]


def rank(x):
    """
    Purpose:
        Return sample ranks of the corresponding elements of x when sorted
        from greatest to smallest. Ties keep original order.

    Parameters:
        x (iterable): Iterable of numeric elements.

    Returns:
        list[int]:
            ranks[i] is the rank (1 = greatest, n = smallest) of x[i].
    """
    n = len(x)
    ord_idx = order(x)  

    ranks = [0] * n
    for r, idx in enumerate(ord_idx, start=1):
        ranks[idx] = r
    return ranks

