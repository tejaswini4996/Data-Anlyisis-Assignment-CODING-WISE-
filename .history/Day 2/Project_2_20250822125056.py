def certi(Statement,Assignment,LIVE_class,Camera_On):
    if Statement == "All Day" and  LIVE_class == "attented" and Camera_On == "yes":
        if Assignment == "completed":  
            return "Eligiible for certificate"
        else:
            return "Not eligible for certificate"
    else: return "Not eligible"

print(certi("All Day","completed","attended","yes"))    