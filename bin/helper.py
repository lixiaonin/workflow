def size_readable(num, suffix='B'):
    """
    Convert file size number to human readable string.
    largest unit: PB
    """
    for unit in ['','K','M','G','T','P']:
        if abs(num) < 1024.0: 
            return "%3.1f%s%s" % (num, unit, suffix) 
        num /= 1024.0 
    return "%.1f %s%s" % (num, 'Yi', suffix)
