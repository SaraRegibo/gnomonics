import math

def getSubStyleDistance(latitude, declination):
    
    """
    PURPOSE: Finding the sub-style distance SD for the given latitude and the given
             declination of the wall.
                 
    INPUT:
        - latitude: Latitude of the place where the subdials is to be installed [degrees].
        - declination: Declination of the wall on which the sundials is to be installed [degrees].
        
    OUTPUT: Sub-style distance SD, as in Eq. (2) on p79 in Waugh 1973.
    """

    # log(tan(SD)) = log(sin(D)) + log(cot(phi)) = log(sin(D) * cot(phi))
    
    sinDecl = math.sin(math.radians(declination))
    cotLat = 1.0 / math.tan(math.radians(latitude))
    
    tanSD = (sinDecl * cotLat)
    
    return math.degrees(math.atan(tanSD))


def getStyleHeight(latitude, declination):

def getLongitudeDifference(latitude, declination):

def getAngleAV(latitude, declination):

def getHourLines():

