import csv

def main():
    with open("WellMain.csv") as wellmain:
        with open("WaterLevelsCombination.csv") as waterlevel:
            with open("WellMain_optimized.csv", 'w') as f:

                writer = csv.writer(f)
                arr = ["StateWellNumber","County","RiverBasin","Aquifer","Latitude","Longitude","Owner","Driller","WellUse","DrillingMonth","DrillingDay","DrillingYear","MeasurementMonth","MeasurementDay","MeasurementYear","WellDepth","LandElevation","DepthFromLSD","WaterElevation"]
                writer.writerow(arr)

                wm = wellmain.readline()
                wl = waterlevel.readline()

                wl = waterlevel.readline().split(",")
                wm = wellmain.readline().split(",")

                d = {}

                while len(wm) > 1:

                    if( wm[22] != "" ):
                        arr = [wm[2]]
                        arr.append(wm[11])
                        arr.append(wm[15])
                        arr.append(wm[20])
                        arr.append(wm[21])
                        arr.append(wm[36])
                        arr.append(wm[27])
                        arr.append(wm[28])
                        arr.append(wm[29])
                        arr.append(wm[22])
                        d[wm[0].lstrip("0")] = arr

                    wm = wellmain.readline().split(",")
                
                while len(wl) > 1:

                    k = wl[0].lstrip("0")

                    if( k in d and wl[10] != "" and wl[9] != "" and wl[12] != "" ):
                        arr = [k,wl[1],d[k][0],wl[2],d[k][1],d[k][2],d[k][3],d[k][4],d[k][5],d[k][6],d[k][7],d[k][8],wl[4],wl[5],wl[6],d[k][9],wl[10],wl[9],wl[12]]
                        writer.writerow(arr)

                    wl = waterlevel.readline().split(",")

if __name__ == "__main__":
    main()