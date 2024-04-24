from Code_dieu_khien.Motors_control import forward,backward,setServoAngle,turnOfCar,changePwm,beInLane #,stop
import config
import cv2
import i2c_comunicate as i2c

angle_of_car = 1
car_turn_angle = 1
def Steer(Distance,Curvature,frame , Mode , Tracked_class):
    if config.Testing:
        if(Distance != -1000 | Curvature != -1000):
            if (config.debugging):
                angle_of_car , current_speed = beInLane(int(frame.shape[1]/4), Distance, Curvature ,Mode ,Tracked_class )
                angle_speed_str = "[ Goc ,Van_Toc ] = [ " + str(int(angle_of_car)) + " , " + str(int(current_speed)) + " ] "
                #cv2.putText(frame_disp,str(angle_of_car),(frame.shape[1]-400,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,255),2)
                cv2.putText(frame,str(angle_speed_str),(20,20),cv2.FONT_HERSHEY_DUPLEX,0.4,(0,0,255),1)
                return angle_of_car


    else:
        if(Distance != -1000 | Curvature != -1000):
            if (config.debugging):
                
                angle_of_car, current_speed= beInLane(int(frame.shape[1]/4), Distance,Curvature  , Mode , Tracked_class)
                return angle_of_car

    
def Drive_Car(Current_State):
    [distance, Curvature, frame_disp, Mode, Tracked_class] = Current_State
    car_turn_angle = int(Steer(distance, Curvature,frame_disp, Mode, Tracked_class))
    i2caddress1= 0x01
    #i2caddress2= 0x00
    i2c.i2c(i2caddress1, car_turn_angle)
    #i2c.i2c(i2caddress2, car_turn_angle)"""
    print("car_turn_angle: ", car_turn_angle)
    #return car_turn_angle
    
    



    
