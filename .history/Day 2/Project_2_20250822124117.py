def certi(Statement):
    if Statement == "All Day":
        if Assignment == completed:
            return "Eligiible for certificate"
        else:
            return "Not eligible for certificate"
        
        if LIVE_class == Attented:
            return "Eligible for certificate"
        else:
            return "Not eligible"
        if Camera_On == Yes :
            return "Eligible for certificate"
        else:
            return "Not eligible for certificate"
    else:
        return "Not eligible"    


print(certi("All Day"))    