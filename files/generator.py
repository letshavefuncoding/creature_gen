import json
import random as r
"""generating a monstrosity for games"""
def jRead(jsfile):
    intake=open(jsfile)
    output=json.load(intake)
    return output
def gensettings():
    settings=[]
    size=r.randint(1,3)
    Base_Creature=r.randint(1,7)
    Special_Body_quality=0
    Body_quality=r.randint(1,4)
    Legs=r.randint(1,3)
    Leg_stat=0
    Special_trait=r.randint(1,11) 
    material=r.randint(1,3)
    Special_Material=0
    """ eyes=r.randint(1,2)
    eye_count=0"""
    if(material==3):
        Special_Material=r.randint(1,20)
    """if(eyes==2):
        eye_count=r.randint(1,8)"""
    if(Body_quality==4):
        Special_Body_quality=r.randint(1,4)
    if(Legs==3):
        Leg_stat=r.randint(1,8)
    settings.append(size)
    settings.append(Base_Creature)
    settings.append(Special_Body_quality)
    settings.append(Leg_stat)
    settings.append(Special_trait)
    settings.append(Special_Material)
    """ settings.append(eye_count)"""
    return settings
def creatureset(settings):
    """take the numbers generated in settings, and correlate them to IDs in the json files"""
    """final[ 0:size, 1:basecreature,2:specialbody quality,3:limb_count, 4:special traits,
    5:Special Material, 6: number of eyes ]"""
    final=[]
    creature=jRead("files/jsons/basecreature.json")
    si=jRead("files/jsons/size.json")
    bq=jRead("files/jsons/shape_legs_eyes.json")
    tra=jRead("files/jsons/traits.json")
    mats=jRead("files/jsons/materials.json")

    for sizes in si["size"]:
        if sizes["ID"]==settings[0]:
            final.append("size: "+sizes["size"])
    for creatures in creature["Creatures"]:
        if creatures["ID"]==settings[1]:
            final.append("Species: "+creatures["Species"])
    if settings[2]!=0:
          for shape in bq["Quality"]:
              if shape["ID"]==settings[2]:
                  final.append("Body Descirption: "+shape["Des"])
    else:
        final.append("normal apperance")
    for legstat in bq["limbs"]:
        if legstat["ID"]==settings[3]:
            final.append("Limbs: "+legstat["Animal"])
    for trait in tra["traits"]:
        if trait["ID"]==settings[4]:
            final.append("Special trait: "+ trait["Name"])
    if settings[5]!=0:
        for mat in mats["material"]:
            if mat["ID"]==settings[5]:
                final.append("special_material: "+mat["Name"])

    return final
def cRead(creature):
    for piece in creature:
        print(piece+"\n")

def main():
    settings=gensettings()
    c=creatureset(settings)
    """cRead(c)"""
    return c