#include "DHT.h"  //所需头文件 
#define DHTPIN  2 //温湿度传感器所接数据引脚号 
#define DHTTYPE DHT11  //温湿度传感器型号  
DHT dht(DHTPIN, DHTTYPE); 
int hum = 0, temp = 0 ;
int ledR,ledG,ledB;

#include <Wire.h> 
#include <BH1750.h>  //所需头文件 
BH1750 lightMeter; //定义一个光照传感器类型 
int lux = 0 ; //光照变量

int flag;
int msg[20]={0},set1[20]={0};

//导入各头文件、符号常量及各变量定义 
void setup() 
    { 
      Serial.begin(9600);
      dht.begin();
      Wire.begin();
      lightMeter.begin();
      
    } 
void loop() 
{  
   delay(500);
   sensorread();
   int count;
    while (Serial.available() > 0) //判断是否有待接收的数据 
    { 
    
    msg[count]=Serial.read();
    if (msg[count] != 'T') {flag=1;}  //判断是否是数据结束标志 
    if (flag == 1)    
      { 
        datamanage();  
      } 
    
    }
} 

void datamanage() 
{ 
    for (char k = 0 ; k < 11; k++)    
    {  
        
          
         if (msg[k] == 'G')            
          {
            
             for (int i=1;i<9;i++)
               {
                  set1[i]=int(Serial.read())-48;
               }
             ledR=set1[1]*100+set1[2]*10+set1[3];
             ledG=set1[4]*100+set1[5]*10+set1[6];
             ledB=set1[7]*100+set1[8]*10+set1[9];
             RGBset(ledR, ledG, ledB); 
          }
    flag = 0; 
}
}

void sensorread() 
{ 
   hum = dht.readHumidity(); 
   temp = dht.readTemperature(); 
   lux = lightMeter.readLightLevel(); 
  
   Serial.print(temp);
   Serial.print(",");
   Serial.print(hum);
   Serial.print(",");
   Serial.println(lux);
    
}

 
void RGBset(int ledr,int ledg,int ledb) 
{ 
  analogWrite(3, ledr);
  analogWrite(5, ledg);
  analogWrite(6, ledb);
} 
