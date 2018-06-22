import math

def getSubStyleDistance(latitude, declination):
    
    """
    PURPOSE: Finding the sub-style distance SD for the given latitude and the given
             declination of the wall.
                 
    INPUT:
        - latitude: Latitude of the place where the subdials is to be installed [degrees].
        - declination: Declination of the wall on which the sundials is to be installed [degrees].
        
    OUTPUT: Sub-style distance SD, as in Eq. (1) on p79 in Waugh 1973.
    """

    # log(tan(SD)) = log(sin(D)) + log(cot(phi)) = log(sin(D) * cot(phi)) = log(sin(D) / tan(phi))
    
    sinDecl = math.sin(math.radians(declination))
    cotLat = 1.0 / math.tan(math.radians(latitude))
    
    tanSD = (sinDecl * cotLat)
    
    return math.degrees(math.atan(tanSD))





def getStyleHeight(latitude, declination):

    """
    PURPOSE: Finding the style height SH for the given latitude and the given
             declination of the wall.
        
    INPUT:
        - latitude: Latitude of the place where the subdials is to be installed [degrees].
        - declination: Declination of the wall on which the sundials is to be installed [degrees].
        
    OUTPUT: Style height SH, as in Eq. (2) on p79 in Waugh 1973.
    """

    # log(sin(SH)) = log(cos(D)) + log(cos(phi))

    cosDecl = math.cos(math.radians(declination))
    cosLat = math.cos(math.radians(latitude))

    sinSH = cosDecl * cosLat

    return math.degrees(math.asin(sinSH))





def getLongitudeDifference(latitude, declination):

    """
    PURPOSE: Finding the difference in latitude DL for the given latitude and the given
    declination of the wall.
    
    INPUT:
    - latitude: Latitude of the place where the subdials is to be installed [degrees].
    - declination: Declination of the wall on which the sundials is to be installed [degrees].
    
    OUTPUT: Difference in latitude DL, as in Eq. (3) on p79 in Waugh 1973.
    """

    # log(cot(DL)) = log(cot(D)) + log(sin(phi)) = log(1 / tan(D)) + log(sin(phi))

    cotDecl = 1.0 / math.tan(math.radians(declination))
    sinLat = math.sin(math.radians(latitude))

    tanDL = 1.0 / (cotDecl * sinLat)

    return math.degrees(math.atan(tanDL))





def getAngleAV(latitude, declination):

    """
    PURPOSE: Finding the angle between the lines for 12pm and 6pm  for the given
             latitude and the given declination of the wall.
    
    INPUT:
    - latitude: Latitude of the place where the subdials is to be installed [degrees].
    - declination: Declination of the wall on which the sundials is to be installed [degrees].
    
    OUTPUT: Angle AV, as in Eq. (4) on p79 in Waugh 1973.
    """

    # log(cot(AV)) = log(sin(D)) + log(tan(phi))

    sinDecl = math.sin(math.radians(declination))
    tanLat = math.tan(math.radians(latitude))

    cotAV = sinDecl * tanLat

    return math.degrees(math.atan(1.0 / cotAV))





#def getHourLines():

