from django.shortcuts import render
from django.shortcuts import HttpResponse


def mission(request):
    msg = "<h2> MISSION </h2> <br/> The College of Computer Studies shall produce technically competent Informations Technology professions adequate prepared in the practice of their profession supportive of national development goals and standards of global excellence"
    return HttpResponse(msg);

def vision(request):
    msg = "<h2> VISION </h2> <br/> The College of Computer Studies shall be a Center of excellence in Information Technology education."
    return HttpResponse(msg);

def objectives(request):
    msg = "<h2> OBJECTIVES </h2> <br/> After graduation, alummi of MSEUF-CCS program shall: <br/> 1. Be employed and demonstate professionalism, competence and passion in solving contempporaty computing problems by developing or utilizing innovatives IT solusion. <br/> 2. Embark in lifelong learning or research to attune to the continues innovation in the IT industry in order to adapt to the changing demands of the global market: and <br/> 3. Exhibit leadership and teamwork and commitment to their respective local or global organizations." 
    return HttpResponse(msg);