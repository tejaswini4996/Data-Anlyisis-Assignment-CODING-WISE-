def certi(Statement,Assignment,LIVE_class,Camera_On):
    if Statement == "All Day" :
        if Assignment == "completed"and  LIVE_class == "attended" and Camera_On == "yes":  
            return "Eligiible for certificate"
        else:
            return "Not eligible for certificate"
    else: return "Not eligible"

print(certi("All Day","completed","attended","yes"))    