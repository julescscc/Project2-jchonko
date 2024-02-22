from direct.showbase.ShowBase import ShowBase
import sys
import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths


class SpaceJam(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

        self.accept('escape', self.quit)


    def SetupScene(self):

        #Universe, Planets, Spaceship, Space Station setup
        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/universe.jpg", (0, 0, 0), 10000)
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "./Assets/Planets/planet1.jpg", (-6000, -3000, -800), 250)
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "./Assets/Planets/planet2.jpg", (0, 6000, 0), 300)
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "./Assets/Planets/planet3.jpg", (500, -5000, 200), 500)
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "./Assets/Planets/planet4.jpg", (300, 6000, 500), 150)
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "./Assets/Planets/planet5.jpg", (700, -2000, 100), 500)
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "./Assets/Planets/planet6.jpg", (0, -900, -1400), 700)
        self.Spaceship = spaceJamClasses.Spaceship(self.loader, "./Assets/Spaceships/Khan/Khan.x", self.render, 'Spaceship', "./Assets/Spaceships/Khan/Khan.jpg", (100, -1000, -100), 1)
        self.SpaceStation = spaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/SpaceStation/spaceStation.x", self.render, 'SpaceStation', "./Assets/Space Station/SpaceStation/SpaceStation1_Dif2.png", (500, -1000, 0), 30)
        self.Player = spaceJamClasses.Player(self.loader, "./Assets/Spaceships/Khan/Khan.x", self.render, 'Player', "./Assets/Spaceships/Khan/Khan.jpg", (0, 0, 0), 1)

        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount +- 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.Planet2, nickName, j, fullCycle, 2)
            self.DrawXYplane(self.Planet4, nickName, j, fullCycle)
            self.DrawXZplane(self.Planet4, nickName, j, fullCycle)
            self.DrawYZplane(self.Planet4, nickName, j, fullCycle)

    def DrawCloudDefense(self, centralObject, droneName):
            unitVec = defensePaths.Cloud()
            unitVec.normalize()
            position = unitVec * 500 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/DroneDefender/octotoad1_auv.png", position, 10)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
            unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
            unitVec.normalize()
            position = unitVec * radius * 250 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawXYplane(self, centralObject, droneName, step, num):
            unitVec = defensePaths.XYplane(step, num)
            unitVec.normalize()
            position = unitVec * 250 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawXZplane(self, centralObject, droneName, step, num):
            unitVec = defensePaths.XZplane(step, num)
            unitVec.normalize()
            position = unitVec * 250 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawYZplane(self, centralObject, droneName, step, num):
            unitVec = defensePaths.YZplane(step, num)
            unitVec.normalize()
            position = unitVec * 250 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/Drone Defender/DroneDefender/octotoad1_auv.png", position, 5)


    def quit(self):
        sys.exit()


app = SpaceJam()
app.run()