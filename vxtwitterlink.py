def vxtwitterlinkfunc(xtwitterlink):
    #define xtwitter and vxtwitter urls
    xtwitterurl = "https://x.com/"
    vxtwitterurl = "https://vxtwitter.com/"

    #If link is good replace with vxtwitter link and return string
    if  xtwitterurl in xtwitterlink:
        vxtwitterlink = xtwitterlink.replace(xtwitterurl, vxtwitterurl)
        return vxtwitterlink
    #check to see if it is a twitter link if not return -1
    else:
      return -1