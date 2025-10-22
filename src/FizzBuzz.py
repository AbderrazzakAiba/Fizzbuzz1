def fizzbuzz(nombre):
    if (nombre % 3 == 0) and (nombre % 5 == 0):
        return "fizzbuzz"
    if (nombre %3 !=0) and (nombre %5!=0) :
        return nombre
    return "fizzbuzz"
