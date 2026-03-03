---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-03T19:57:20.303270+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** March 03, 2026 at 19:57 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A self-driving bike by Agibot founder Peng Zhihui. The design is open sourced & available on Github](https://www.reddit.com/r/robotics/comments/1rjoii6/a_selfdriving_bike_by_agibot_founder_peng_zhihui/)**

GitHub: https://github.com/peng-zhihui/XUAN/blob/main/enREADME.md

7h ago

---

**[Automated greenhouse to grow food](https://www.reddit.com/r/robotics/comments/1rj6h1e/automated_greenhouse_to_grow_food/)**

22h ago

---

**[Zero Actuators, 70% Obstacle Clearance - Passive Claw-Wheel Mechanism Demo](https://www.reddit.com/r/robotics/comments/1riygtc/zero_actuators_70_obstacle_clearance_passive/)**

1d ago

---

**[This tutorial demonstrates how to set up multi-camera VSLAM with Isaac ROS Visual SLAM using multiple RealSense cameras with hardware synchronization!](https://www.reddit.com/r/robotics/comments/1rjsd4p/this_tutorial_demonstrates_how_to_set_up/)**

https://nvidia-isaac-ros.github.io/concepts/visual_slam/cuvslam/tutorial_multi_realsense.html

4h ago

---

**[Singularity avoidance hack: Instead of damping, temporarily lock a joint in wrist singularity for palletizing/pick&place? Anyone tried this?](https://www.reddit.com/r/robotics/comments/1rjpfaf/singularity_avoidance_hack_instead_of_damping/)**

I've been messing with singularity handling in 6 DoF industrial arms, especially for fast palletizing and long-reach pick-and-place. Damped Least Squares (DLS/SDLS) is the go-to, but near wrist singularities it often gets too "mushy" tracking slows down unpredictably, velocities scale weirdly, and in high-speed cycles that can mess up cycle time or stack accuracy. My idea is that instead of damping the whole Jacobian, when det(J) drops below a threshold (say ~0.01–0.05, tunable), hard-lock the problematic joint (usually J5 in typical roll-pitch-roll wrists). Treat the arm as 5 DoF temporarily: Update DH params on the fly (locked joint becomes fixed link). Recompute IK with reduced 6×5 Jacobian. Prioritize task-space: keep XYZ + pitch/yaw solid, sacrifice roll if needed (most palletizing doesn't care about full orientation anyway). Then, when manipulability improves, blend the joint back in smoothly to avoid jerk. Why bother over SDLS? Predictable: you know exactly what you're losing (e.g., "loses roll near vertical stacks"). No infinite velocity risk since you just remove the DoF instead of damping it softly. Cheaper compute: lower-order IK is faster than SVD every cycle. But i have some questions that demand some practical experience with this kind of problem/ideia: Has anyone done on-the-fly kinematic chain changes / joint locking like this? How do you smooth the lock/unlock transition to kill jerk? Exponential blend? Low-pass on velocities? Industrial controllers (KUKA, FANUC, ABB) are super locked down, so is this only feasible in open setups like ROS or custom controls? Any tricks to fake it on proprietary ones? In real production, is the mushiness of DLS actually a big pain (e.g., path deviation stacking boxes wrong), or does damping usually do the job fine and I'm overcomplicating? Feels like a pragmatic dirty hack for certain apps, but could also be a mechanical nightmare if the blend sucks or you lock at the wrong time. Thoughts? "Don't do this" reasons? Would love to hear before I sim/prototype it. Thanks!

6h ago

---

**[Open-source DDS middleware in Rust with robot swarm, LiDAR SLAM, and drone racing demos](https://www.reddit.com/r/robotics/comments/1rjrw8u/opensource_dds_middleware_in_rust_with_robot/)**

Releasing HDDS -- a complete DDS (Data Distribution Service) implementation built from scratch in Rust. For the robotics crowd, the relevant demos: - **Robot Swarm** -- 12 boids with 6 behavior modes (flocking, formation, patrol...), fully decentralized via DDS pub/sub - **LiDAR SLAM** -- autonomous maze mapping with occupancy grid, frontier exploration, all sensor data over DDS - **Drone Racing** -- 6 AI drones navigating gates independently, 60Hz position updates, zero central controller - **F1Tenth Racing** -- bicycle model physics, AI waypoint following with Menger curvature braking DDS is the standard middleware in military robotics and autonomous systems. HDDS is a fully open-source alternative to RTI Connext. Also includes a ROS2 RMW layer (rmw_hdds) if you want to plug it into your existing ROS2 stack. - Source: github.com/hdds-team - Demos: packs.hdds.io

4h ago

---

**[Control board for 6-Axis robot](https://www.reddit.com/r/robotics/comments/1rjb7kt/control_board_for_6axis_robot/)**

I’ve just finished the soldering for the controller for my 6-axis robot. You may notice that there are only 5 drivers and that is because two went bad and I’m waiting on replacements. I also installed the I2C MUX that will interface with the magnetic encoders. Please leave any questions, comments, or advice in the comments, I really appreciate it! More updates on the way.

18h ago

---

**[What would you say about a 17yr old building a humanoid robot?](https://www.reddit.com/r/robotics/comments/1rjpy3q/what_would_you_say_about_a_17yr_old_building_a/)**

I’m currently building a 1,68m tall humanoid robot from scratch as a solo project. I designed and assembled the mechanical structure myself, including the arms and torso, and I’m now working on the legs. It’s going to be battery powered and uses actuators and modules (no custom PCBs). I’m also developing the AI architecture myself. I won’t go into too much detail on that yet, since I’d rather see if I can fully implement it before making big claims. This is my first project at this scale. My goal isn’t maximum strength or industrial-level performance, but creating a functional humanoid platform with its own evolving AI system. I’m turning 17 this year, and I’m building this independently.

6h ago

---

**[Intrinsic AI for Industry Challenge Toolkit has Dropped -- Full cable insertion simulation with hooks for training your own policy.](https://www.reddit.com/r/robotics/comments/1rj9yvn/intrinsic_ai_for_industry_challenge_toolkit_has/)**

Competition toolkit is available here. With additional context on Open Robotics Discourse. Competition details can be found here. Two competition sessions will be held tomorrow, March 3rd (they will be recorded). Session 1: March 3rd: 9-10am PT / 5-6pm UTC (US/Europe friendly) Session 2: March 3rd: 5-6pm PT / March 4th 1-2 am UTC (US/APAC friendly)

19h ago

---

**[Need help for coding line following robot](https://www.reddit.com/r/robotics/comments/1rjv00x/need_help_for_coding_line_following_robot/)**

So i am making a line following car with stm32f401cc black pill board with tb6612fng driver ,n20 500 rpm motors , lipo 3s battery , 12 channel cny70 ir sensor array ,0.92inch oled, four buttons(up,down,back,select) ,a multiplexer also and a buck convertor . So currently i am facing a issue that when i select my calibration tab in setting and calibrate the sensors i works but when i try to save the setting the robot freezes and i am not good with coding so i use a code from a fellow person on github and give it to claude to make it for stm . I appreciate if somebody help me with the code . #include <Wire.h> #include <Adafruit_GFX.h> #include <Adafruit_SSD1306.h> #include <EEPROM.h> // ==================== PINS ==================== #define S0 PB12 #define S1 PB13 #define S2 PB14 #define S3 PB15 #define SIG_PIN PA0 #define BTN_UP PA1 #define BTN_DOWN PA2 #define BTN_SELECT PA3 #define BTN_BACK PA4 #define AIN1 PA5 #define AIN2 PA6 #define PWMA PB8 #define BIN1 PA7 #define BIN2 PB0 #define PWMB PB9 #define STBY PA15 // ==================== OLED ==================== #define SCREEN_WIDTH 128 #define SCREEN_HEIGHT 64 Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1); // ==================== SENSORS ==================== const int SENSOR_COUNT = 13; int sensorValues[SENSOR_COUNT]; int sensorRaw[SENSOR_COUNT]; int weights[13] = {100,200,300,400,500,600,700,800,900,1000,1100,1200,1300}; int position = 700; // ==================== CALIBRATION ==================== int calMin[13], calMax[13]; bool calibrated = false; // ==================== AUTO-INVERSE ==================== int linePolarity = 0; int consecutiveInverseCount = 0; const int INVERSE_CONFIRM = 3; // ==================== PID ==================== float Kp = 2, Ki = 0, Kd = 2; int lastError = 0; float integral = 0; int baseSpeed = 120; int fullSpeed = 170; int errorWindow = 50; // ==================== LOST LINE ==================== unsigned long lostStartTime = 0; const unsigned long lostTimeout = 30; // ==================== SETTINGS ==================== int trackMode = 0; int speedValue = 150; int sensorThreshold = 600; int KpValue = 2; int KdValue = 2; // ==================== RACE TIMER ==================== unsigned long raceStartTime = 0; unsigned long lastLapTime = 0; // ==================== SCREENS ==================== #define SCR_MAIN 0 #define SCR_SETTINGS 1 #define SCR_SENSORBAR 2 #define SCR_CALIBRATE 3 #define SCR_RESULT 4 #define SCR_RUNNING 5 #define SCR_SAVING 6 // NEW: animated saving screen int screen = SCR_MAIN; int screenAfter = SCR_MAIN; // where to go after save completes int mainSel = 0; int settingsSel = 0; // ==================== SAVING STATE MACHINE ==================== // EEPROM writes are done ONE BYTE PER LOOP TICK, so the display // stays alive and the animation runs smoothly with zero lag. enum SavePhase { SAVE_IDLE, SAVE_SETTINGS, // writing the 8 settings bytes/words SAVE_CALDATA, // writing calMin[]/calMax[] arrays (optional) SAVE_CALFLAG, // writing the calibrated flag byte SAVE_DONE // final tick: transition to screenAfter }; SavePhase savePhase = SAVE_IDLE; int saveIdx = 0; // index within the current phase bool saveCal = false; // also save calibration data? // Saving animation unsigned long saveAnimMs = 0; int saveAnimDot = 0; // 0..3 cycling dots unsigned long saveStartMs = 0; // ==================== CALIBRATION SUB-STATE ==================== enum CalState { CAL_IDLE, CAL_RUNNING, CAL_DONE }; CalState calState = CAL_IDLE; unsigned long calStartMs = 0; // ==================== DEBOUNCE ==================== unsigned long btnTime[4] = {0,0,0,0}; const int BTN_PINS[4] = {BTN_UP, BTN_DOWN, BTN_SELECT, BTN_BACK}; const unsigned long DEBOUNCE = 180; unsigned long lastRunDisp = 0; unsigned long lastSnsDisp = 0; unsigned long lastCalDisp = 0; // ==================== EEPROM MAP ==================== #define EE_TRACKMODE 0 #define EE_SPEED 1 #define EE_THRESHOLD 2 // 2 bytes #define EE_KP 4 // 2 bytes #define EE_KD 6 // 2 bytes #define EE_ERRWIN 8 // 2 bytes #define EE_CALMIN 10 // 13*2 = 26 bytes #define EE_CALMAX 36 // 13*2 = 26 bytes #define EE_CALIBRATED 62 // ===================================================================== // BUTTON helper // ===================================================================== bool btnEdge(int idx) { if (digitalRead(BTN_PINS[idx]) == LOW) { if (millis() - btnTime[idx] > DEBOUNCE) { btnTime[idx] = millis(); return true; } } return false; } #define UP_PRESS btnEdge(0) #define DOWN_PRESS btnEdge(1) #define SEL_PRESS btnEdge(2) #define BACK_PRESS btnEdge(3) // ===================================================================== // SENSORS // ===================================================================== int readMux(int ch) { digitalWrite(S0, (ch >> 0) & 1); digitalWrite(S1, (ch >> 1) & 1); digitalWrite(S2, (ch >> 2) & 1); digitalWrite(S3, (ch >> 3) & 1); delayMicroseconds(50); return analogRead(SIG_PIN); } void readSensorsRaw() { for (int i = 0; i < SENSOR_COUNT; i++) sensorRaw[i] = readMux(i); } void applyPolarity() { for (int i = 0; i < SENSOR_COUNT; i++) { int v = (sensorRaw[i] > sensorThreshold) ? 1 : 0; sensorValues[i] = (linePolarity == 0) ? v : 1 - v; } } void readSensors() { readSensorsRaw(); applyPolarity(); } int calcPosition() { int num = 0, den = 0; for (int i = 0; i < SENSOR_COUNT; i++) { num += sensorValues[i] * weights[i]; den += sensorValues[i]; } return (den == 0) ? position : (num / den); } void autoInverse() { int bright = 0; for (int i = 0; i < SENSOR_COUNT; i++) if (sensorRaw[i] > sensorThreshold) bright++; int detected = (bright > SENSOR_COUNT / 2) ? 0 : 1; if (detected != linePolarity) { if (++consecutiveInverseCount >= INVERSE_CONFIRM) { linePolarity = detected; consecutiveInverseCount = 0; applyPolarity(); } } else { consecutiveInverseCount = 0; } } // ===================================================================== // MOTORS // ===================================================================== void setMotorSpeed(int L, int R) { if (L >= 0) { digitalWrite(AIN1,HIGH); digitalWrite(AIN2,LOW); } else { digitalWrite(AIN1,LOW); digitalWrite(AIN2,HIGH); L=-L; } if (R >= 0) { digitalWrite(BIN1,HIGH); digitalWrite(BIN2,LOW); } else { digitalWrite(BIN1,LOW); digitalWrite(BIN2,HIGH); R=-R; } analogWrite(PWMA,L); analogWrite(PWMB,R); } void stopMotors() { digitalWrite(AIN1,LOW); digitalWrite(AIN2,LOW); digitalWrite(BIN1,LOW); digitalWrite(BIN2,LOW); analogWrite(PWMA,0); analogWrite(PWMB,0); } void spinRightSlow() { digitalWrite(AIN1,HIGH); digitalWrite(AIN2,LOW); digitalWrite(BIN1,LOW); digitalWrite(BIN2,HIGH); analogWrite(PWMA,150); analogWrite(PWMB,150); } void spinLeftSlow() { digitalWrite(AIN1,LOW); digitalWrite(AIN2,HIGH); digitalWrite(BIN1,HIGH); digitalWrite(BIN2,LOW); analogWrite(PWMA,150); analogWrite(PWMB,150); } // ===================================================================== // EEPROM — applySettings + loadSettings stay blocking (only at boot) // saveSettings is now SPLIT into the async state machine. // ===================================================================== void applySettings() { baseSpeed = speedValue; fullSpeed = constrain(speedValue + 50, 50, 255); Kp = KpValue; Kd = KdValue; linePolarity = (trackMode == 0) ? 0 : 1; } void loadSettings() { trackMode = EEPROM.read(EE_TRACKMODE); if (trackMode > 1) trackMode = 0; speedValue = EEPROM.read(EE_SPEED); if (speedValue < 50 || speedValue > 255) speedValue = 120; EEPROM.get(EE_THRESHOLD, sensorThreshold); if (sensorThreshold < 50 || sensorThreshold > 4000) sensorThreshold = 600; EEPROM.get(EE_KP, KpValue); if (KpValue < 0 || KpValue > 100) KpValue = 2; EEPROM.get(EE_KD, KdValue); if (KdValue < 0 || KdValue > 100) KdValue = 2; EEPROM.get(EE_ERRWIN, errorWindow); if (errorWindow < 0 || errorWindow > 300) errorWindow = 50; calibrated = (EEPROM.read(EE_CALIBRATED) == 1); if (calibrated) { for (int i = 0; i < SENSOR_COUNT; i++) { EEPROM.get(EE_CALMIN + i * 2, calMin[i]); EEPROM.get(EE_CALMAX + i * 2, calMax[i]); } } applySettings(); } // ---- Start a non-blocking save sequence ---- // withCal = true → also writes calibration arrays + flag // goTo = which screen to show when done void beginSave(bool withCal, int goTo) { saveCal = withCal; screenAfter = goTo; savePhase = SAVE_SETTINGS; saveIdx = 0; saveStartMs = millis(); saveAnimMs = millis(); saveAnimDot = 0; applySettings(); // update RAM immediately so robot uses new values screen = SCR_SAVING; drawSaving(); } // ---- Tick: called every loop(), writes ONE value per call ---- // Returns true when fully done. bool tickSave() { switch (savePhase) { case SAVE_SETTINGS: // Write the 6 settings in sequence, one per tick switch (saveIdx) { case 0: EEPROM.write(EE_TRACKMODE, trackMode); break; case 1: EEPROM.write(EE_SPEED, speedValue); break; case 2: EEPROM.put (EE_THRESHOLD, sensorThreshold);break; case 3: EEPROM.put (EE_KP, KpValue); break; case 4: EEPROM.put (EE_KD, KdValue); break; case 5: EEPROM.put (EE_ERRWIN, errorWindow); break; } saveIdx++; if (saveIdx >= 6) { saveIdx = 0; savePhase = saveCal ? SAVE_CALDATA : SAVE_DONE; } break; case SAVE_CALDATA: // Write ONE calMin + calMax pair per tick (13 ticks total) if (saveIdx < SENSOR_COUNT) { EEPROM.put(EE_CALMIN + saveIdx * 2, calMin[saveIdx]); EEPROM.put(EE_CALMAX + saveIdx * 2, calMax[saveIdx]); saveIdx++; } else { saveIdx = 0; savePhase = SAVE_CALFLAG; } break; case SAVE_CALFLAG: EEPROM.write(EE_CALIBRATED, 1); savePhase = SAVE_DONE; break; case SAVE_DONE: savePhase = SAVE_IDLE; screen = screenAfter; // Draw destination screen immediately if (screenAfter == SCR_MAIN) drawMain(); else if (screenAfter == SCR_SETTINGS) drawSettings(); return true; default: break; } return false; } // ===================================================================== // DISPLAY HELPERS // ===================================================================== void formatTime(char* buf, unsigned long ms) { unsigned long mn = ms / 60000; unsigned long sec = (ms / 1000) % 60; unsigned long hms = (ms % 1000) / 10; sprintf(buf, "%02lu:%02lu.%02lu", mn, sec, hms); } // ---- Progress bar width based on save phase ---- int saveProgress() { // Returns 0-100 int total, done; if (!saveCal) { total = 6; done = saveIdx; } else { total = 6 + SENSOR_COUNT + 1; if (savePhase == SAVE_SETTINGS) done = saveIdx; else if (savePhase == SAVE_CALDATA) done = 6 + saveIdx; else if (savePhase == SAVE_CALFLAG) done = 6 + SENSOR_COUNT; else done = total; } return (done * 100) / total; } // ===================================================================== // DRAW FUNCTIONS // ===================================================================== void drawSaving() { // Animated "Saving" screen — called from tickSave() every ~50 ms display.clearDisplay(); display.setTextColor(SSD1306_WHITE); // ── Floppy-disk icon (16×16 at top-center) drawn with primitives ── int ix = 56, iy = 2; display.drawRect(ix, iy, 16, 16, SSD1306_WHITE); // outer shell display.fillRect(ix+2, iy, 12, 5, SSD1306_WHITE); // label slot top display.fillRect(ix+10, iy, 3, 5, SSD1306_WHITE); // write-protect tab display.fillRect(ix+3, iy+8, 10, 7, SSD1306_WHITE); // magnetic disk area display.fillRect(ix+5, iy+9, 6, 5, SSD1306_BLACK); // disk cutout display.fillRect(ix+6, iy+10,4, 3, SSD1306_WHITE); // disk hub // ── "Saving" text with animated dots ── char dotStr[5] = " "; for (int d = 0; d <= saveAnimDot; d++) dotStr[d] = '.'; display.setTextSize(2); display.setCursor(14, 22); display.print("Saving"); display.print(dotStr); // ── Progress bar ── int pct = saveProgress(); int barW = map(pct, 0, 100, 0, 110); display.drawRect(9, 44, 110, 10, SSD1306_WHITE); display.fillRect(9, 44, barW, 10, SSD1306_WHITE); // ── Percentage label ── display.setTextSize(1); display.setCursor(49, 56); display.print(pct); display.print("%"); display.display(); } void drawMain() { display.clearDisplay(); display.setTextSize(1); display.setTextColor(SSD1306_WHITE); display.setCursor(18, 0); display.print("Team Gearheads"); if (calibrated) { display.setCursor(88, 0); display.print("[CAL]"); } const char* items[] = {"START","SETTINGS","SENSOR BAR","CALIBRATE"}; for (int i = 0; i < 4; i++) { display.setCursor(8, 13 + i * 12); display.print(mainSel == i ? "> " : " "); display.print(items[i]); } if (lastLapTime > 0) { char tb[12]; formatTime(tb, lastLapTime); display.setCursor(0, 56); display.print("Last: "); display.print(tb); } display.display(); } void drawSettings() { display.clearDisplay(); display.setTextSize(1); display.setTextColor(SSD1306_WHITE); const char* lbl[] = {"Track:","Speed:","Thresh:","Kp:","Kd:","ErrWin:","SAVE"}; const int N = 7, VIS = 6; int start = constrain(settingsSel - 2, 0, N - VIS); for (int i = 0; i < VIS; i++) { int idx = start + i; display.setCursor(0, i * 10 + 2); display.print(settingsSel == idx ? ">" : " "); display.print(lbl[idx]); switch (idx) { case 0: display.print(trackMode==0?"BLACK":"WHITE"); break; case 1: display.print(speedValue); break; case 2: display.print(sensorThreshold); break; case 3: display.print(KpValue); break; case 4: display.print(KdValue); break; case 5: display.print(errorWindow); break; } } display.setCursor(0, 56); display.print("SEL=+ BACK=-"); display.display(); } void drawRunning() { display.clearDisplay(); display.setTextSize(2); display.setTextColor(SSD1306_WHITE); display.setCursor(5, 0); display.print("RUNNING"); display.setTextSize(1); display.setCursor(0, 18); display.print("Kp:"); display.print(KpValue); display.print(" Kd:"); display.print(KdValue); display.print(" Sp:"); display.print(speedValue); char tb[12]; formatTime(tb, millis() - raceStartTime); display.setCursor(0, 29); display.print("Time: "); display.print(tb); int initPol = (trackMode == 0) ? 0 : 1; if (linePolarity != initPol) { display.setCursor(96, 29); display.print("INV!"); } for (int i = 0; i < SENSOR_COUNT; i++) { int x = i * 9 + 5; if (sensorValues[i]) display.fillRect(x, 40, 8, 10, SSD1306_WHITE); else display.drawRect(x, 40, 8, 10, SSD1306_WHITE); } display.setCursor(18, 54); display.print("BACK = STOP"); display.display(); } void drawSensorBar() { readSensorsRaw(); display.clearDisplay(); display.setTextSize(1); display.setTextColor(SSD1306_WHITE); display.setCursor(22, 0); display.print("SENSOR BAR"); display.setCursor(0, 10); display.print("Thr:"); display.print(sensorThreshold); const int BH = 38, BY = 63; for (int i = 0; i < SENSOR_COUNT; i++) { int x = i * 9 + 5; int h = map(sensorRaw[i], 0, 4095, 2, BH); display.drawRect(x, BY - BH, 8, BH, SSD1306_WHITE); display.fillRect(x, BY - h, 8, h, SSD1306_WHITE); } int thY = BY - map(sensorThreshold, 0, 4095, 2, BH); display.drawFastHLine(5, thY, SENSOR_COUNT * 9, SSD1306_WHITE); display.setCursor(0, 55); display.print("BACK = exit"); display.display(); } void drawCalibrate() { display.clearDisplay(); display.setTextSize(1); display.setTextColor(SSD1306_WHITE); display.setCursor(18, 0); display.print("CALIBRATION"); switch (calState) { case CAL_IDLE: display.setCursor(0, 14); display.println("Sweep robot over"); display.println("black + white areas."); display.println(""); display.println("SELECT = Start"); display.println("BACK = Cancel"); break; case CAL_RUNNING: { unsigned long elapsed = (millis() - calStartMs) / 1000; display.setCursor(0, 14); display.print("Scanning... "); display.print(elapsed); display.println("s"); display.println("Move over all areas"); display.println("SELECT = Finish"); display.println("BACK = Cancel"); for (int i = 0; i < SENSOR_COUNT; i++) { int x = i * 9 + 5; if (sensorRaw[i] > sensorThreshold) display.fillRect(x, 58, 8, 5, SSD1306_WHITE); else display.drawRect(x, 58, 8, 5, SSD1306_WHITE); } break; } case CAL_DONE: display.setCursor(0, 14); display.println("Scan complete!"); display.print("Threshold: "); display.println(sensorThreshold); display.println(""); display.println("SELECT = Save"); display.println("BACK = Discard"); break; } display.display(); } void drawResult() { display.clearDisplay(); display.setTextSize(1); display.setTextColor(SSD1306_WHITE); display.setCursor(25, 0); display.print("RACE DONE!"); char tb[12]; formatTime(tb, lastLapTime); display.setTextSize(2); display.setCursor(5, 14); display.print(tb); display.setTextSize(1); display.setCursor(0, 36); display.print("Kp:"); display.print(KpValue); display.print(" Kd:"); display.print(KdValue); display.print(" Spd:"); display.println(speedValue); int initPol = (trackMode == 0) ? 0 : 1; display.setCursor(0, 46); display.print("AutoInv:"); display.println(linePolarity != initPol ? "Triggered" : "No flip"); display.setCursor(0, 56); display.print("SEL=Retry BACK=Menu"); display.display(); } // ===================================================================== // SETUP // ===================================================================== void setup() { Serial.begin(115200); Wire.begin(); if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { Serial.println(F("SSD1306 failed")); while (true); } display.clearDisplay(); display.display(); loadSettings(); pinMode(S0,OUTPUT); pinMode(S1,OUTPUT); pinMode(S2,OUTPUT); pinMode(S3,OUTPUT); pinMode(AIN1,OUTPUT); pinMode(AIN2,OUTPUT); pinMode(BIN1,OUTPUT); pinMode(BIN2,OUTPUT); pinMode(PWMA,OUTPUT); pinMode(PWMB,OUTPUT); pinMode(STBY,OUTPUT); digitalWrite(STBY, HIGH); pinMode(BTN_UP, INPUT_PULLUP); pinMode(BTN_DOWN, INPUT_PULLUP); pinMode(BTN_SELECT,INPUT_PULLUP); pinMode(BTN_BACK, INPUT_PULLUP); stopMotors(); drawMain(); } // ===================================================================== // LOOP — pure state machine, zero blocking delays // ===================================================================== void loop() { switch (screen) { // ---------------------------------------------------------------- case SCR_MAIN: if (UP_PRESS) { mainSel = (mainSel - 1 + 4) % 4; drawMain(); } if (DOWN_PRESS) { mainSel = (mainSel + 1) % 4; drawMain(); } if (SEL_PRESS) { switch (mainSel) { case 0: lastError = 0; integral = 0; consecutiveInverseCount = 0; linePolarity = (trackMode == 0) ? 0 : 1; raceStartTime = millis(); screen = SCR_RUNNING; drawRunning(); break; case 1: settingsSel = 0; screen = SCR_SETTINGS; drawSettings(); break; case 2: screen = SCR_SENSORBAR; drawSensorBar(); break; case 3: calState = CAL_IDLE; screen = SCR_CALIBRATE; drawCalibrate(); break; } } break; // ---------------------------------------------------------------- case SCR_SETTINGS: { const int N = 7; if (UP_PRESS) { settingsSel = (settingsSel - 1 + N) % N; drawSettings(); } if (DOWN_PRESS) { settingsSel = (settingsSel + 1) % N; drawSettings(); } if (SEL_PRESS) { switch (settingsSel) { case 0: trackMode = (trackMode == 0) ? 1 : 0; break; case 1: speedValue = constrain(speedValue + 10, 50, 255); break; case 2: sensorThreshold = constrain(sensorThreshold + 50, 50, 4000); break; case 3: KpValue = constrain(KpValue + 1, 0, 50); break; case 4: KdValue = constrain(KdValue + 1, 0, 50); break; case 5: errorWindow = constrain(errorWindow + 5, 0, 300); break; case 6: beginSave(false, SCR_MAIN); break; // ← NON-BLOCKING } if (screen == SCR_SETTINGS) drawSettings(); } if (BACK_PRESS) { switch (settingsSel) { case 0: trackMode = (trackMode == 0) ? 1 : 0; break; case 1: speedValue = constrain(speedValue - 10, 50, 255); break; case 2: sensorThreshold = constrain(sensorThreshold - 50, 50, 4000); break; case 3: KpValue = constrain(KpValue - 1, 0, 50); break; case 4: KdValue = constrain(KdValue - 1, 0, 50); break; case 5: errorWindow = constrain(errorWindow - 5, 0, 300); break; case 6: screen = SCR_MAIN; drawMain(); break; } if (screen == SCR_SETTINGS) drawSettings(); } break; } // ---------------------------------------------------------------- case SCR_SENSORBAR: if (millis() - lastSnsDisp > 100) { lastSnsDisp = millis(); drawSensorBar(); } if (BACK_PRESS) { screen = SCR_MAIN; drawMain(); } break; // ---------------------------------------------------------------- case SCR_CALIBRATE: if (calState == CAL_RUNNING) { readSensorsRaw(); for (int i = 0; i < SENSOR_COUNT; i++) { if (sensorRaw[i] < calMin[i]) calMin[i] = sensorRaw[i]; if (sensorRaw[i] > calMax[i]) calMax[i] = sensorRaw[i]; } if (millis() - lastCalDisp > 200) { lastCalDisp = millis(); drawCalibrate(); } } if (SEL_PRESS) { if (calState == CAL_IDLE) { for (int i = 0; i < SENSOR_COUNT; i++) { calMin[i] = 4095; calMax[i] = 0; } calStartMs = millis(); calState = CAL_RUNNING; drawCalibrate(); } else if (calState == CAL_RUNNING) { int sum = 0; for (int i = 0; i < SENSOR_COUNT; i++) sum += (calMin[i] + calMax[i]) / 2; sensorThreshold = sum / SENSOR_COUNT; calibrated = true; calState = CAL_DONE; drawCalibrate(); } else if (calState == CAL_DONE) { calState = CAL_IDLE; beginSave(true, SCR_MAIN); // ← saves settings + cal data, NON-BLOCKING } } if (BACK_PRESS) { calState = CAL_IDLE; screen = SCR_MAIN; drawMain(); } break; // ---------------------------------------------------------------- case SCR_RESULT: if (SEL_PRESS) { lastError = 0; integral = 0; consecutiveInverseCount = 0; linePolarity = (trackMode == 0) ? 0 : 1; raceStartTime = millis(); screen = SCR_RUNNING; drawRunning(); } if (BACK_PRESS) { screen = SCR_MAIN; drawMain(); } break; // ---------------------------------------------------------------- case SCR_RUNNING: runLineFollower(); if (millis() - lastRunDisp > 200) { lastRunDisp = millis(); drawRunning(); } break; // ---------------------------------------------------------------- case SCR_SAVING: // Tick the EEPROM write machine (one value per loop pass) tickSave(); // Refresh the animated display at ~20 fps if (millis() - saveAnimMs > 50) { saveAnimMs = millis(); saveAnimDot = (saveAnimDot + 1) % 4; drawSaving(); } break; } } // ===================================================================== // LINE FOLLOWER // ===================================================================== void runLineFollower() { readSensors(); autoInverse(); int active = 0; for (int i = 0; i < SENSOR_COUNT; i++) active += sensorValues[i]; if (active == SENSOR_COUNT) { stopMotors(); lastLapTime = millis() - raceStartTime; screen = SCR_RESULT; drawResult(); return; } if (active == 0) { if (lostStartTime == 0) lostStartTime = millis(); if (millis() - lostStartTime < lostTimeout) { setMotorSpeed(fullSpeed, fullSpeed); } else { if (lastError > 0) spinRightSlow(); else spinLeftSlow(); } } else { lostStartTime = 0; position = calcPosition(); int error = position - 700; if (abs(error) <= errorWindow) { setMotorSpeed(fullSpeed, fullSpeed); integral = 0; } else { integral = constrain(integral + error, -1000, 1000); int corr = (int)(Kp * error + Ki * integral + Kd * (error - lastError)); setMotorSpeed(constrain(baseSpeed + corr, 0, 255), constrain(baseSpeed - corr, 0, 255)); } lastError = error; } if (BACK_PRESS) { stopMotors(); lastLapTime = millis() - raceStartTime; screen = SCR_RESULT; drawResult(); } }

2h ago

---

---

## Google News: "robotics"

**[China's Honor shows off smartphone with robotic camera arm and teases a humanoid robot](https://www.cnbc.com/2026/03/01/honor-robot-phone-magic-v6-foldable-launch-mwc.html)**

Honor debuted a Robot Phone on Sunday at the Mobile World Congress as it looks to stand out from rivals like Samsung and Apple in the smartphone market.

CNBC • 2d ago

---

**[Why humanoid robots are learning everyday tasks faster than expected](https://www.scientificamerican.com/article/why-humanoid-robots-are-learning-everyday-tasks-faster-than-expected/)**

Roboticist Benjie Holson created the “Humanoid Olympic Games” thinking home robots were 15 years away. Then they started folding the laundry

Scientific American • 1d ago

---

**[China Could Dominate the Physical AI Future](https://time.com/7382151/china-dominates-the-physical-ai-race/)**

Eric Schmidt and Selina Xu argue that China is pulling head of the U.S. in the race to build AI-powered robots.

Time Magazine • 8h ago

---

**[Richtech Robotics (RR) Valuation Check After Recent Share Price Volatility](https://finance.yahoo.com/news/richtech-robotics-rr-valuation-check-191352823.html)**

Richtech Robotics stock overview Richtech Robotics (RR) has been drawing attention after a period of sharp share price swings, with the stock down about 30% over the past month and past 3 months, yet showing a positive 1 year total return. See our latest analysis for Richtech Robotics. At a latest share price of $2.49, Richtech Robotics has seen short term pressure, with a 1 day share price return showing a 9.1% decline and a 30 day share price return showing a 30.5% decline. The 1 year total...

Yahoo Finance • 1d ago

---

**[Studying snakes' ability to stand upright could inform soft robotics and more](https://phys.org/news/2026-03-snakes-ability-upright-soft-robotics.html)**

Phys.org • 2h ago

---

**[Clarksburg Robotics Team Advances to National Competition](https://mocoshow.com/2026/03/01/clarksburg-robotics-team-advances-to-national-competition/)**

A group of Montgomery County students is heading to a national robotics competition after an impressive showing at both the regional and state levels. Team MiniTechs, a robotics team based […]

The MoCo Show - • 1d ago

---

**[Inside of Carnegie Mellon University’s new robotics center, where machines jump, swim and fly](https://www.post-gazette.com/business/tech-news/2026/03/01/carnegie-mellon-university-robotics-center-hazelwood/stories/202603010098)**

The words “robots at work” now line the concrete floor of a three-story warehouse in Hazelwood, where machines on Friday built Lego sets, whizzed...

Pittsburgh Post-Gazette • 1d ago

---

**[Simulated cats and elephants with touch-based memory help usher in new age of robotics](https://techxplore.com/news/2026-03-simulated-cats-elephants-based-memory.html)**

Tech Xplore • 2h ago

---

**[LLM (Claude) Given Robotic Hand Immediately Starts Making Peace Signs](https://blog.adafruit.com/2026/03/02/llm-claude-given-robotic-hand-immediately-starts-making-peace-signs/)**

Adafruit • 1d ago

---

**[STEM meets sports tourism as Robotics Championship plans return to Clarksville](https://clarksvillenow.com/local/stem-meets-sports-tourism-as-robotics-championship-plans-return-to-clarksville/)**

The Vex Robotics competition will take place at F&M Bank Arena, hosting 42 schools fielding 96 teams representing more than 500 middle and high school students.

Clarksville Now • 5h ago

---

---

## YouTube Videos: "robotics"

**[The Most Advanced Pink Robot! #humanoid](https://www.youtube.com/watch?v=Bt_PfCVm9no)**

The Most Advanced Pink Robot! #humanoid ​#BlueRobot #Humanoid #FutureTech #AI #Robotics #Future #SmartMachine.

📺 MSU Channel

👁️ 833 • 👍 2 • ⏱️ 0:19 • 7h ago

---

**[Barcelona MWC 2026 Opens with Humanoid Robots and AI Breakthroughs | APT](https://www.youtube.com/watch?v=fzXFWzHfaz8)**

Day one of Mobile World Congress 2026 in Barcelona spotlighted next-generation robotics and AI innovation. China's AgiBot ...

📺 APT

👁️ 988 • 👍 12 • 💬 2 • ⏱️ 5:34 • 11h ago

---

**[China Unveiled Its First Army of Humanoid Police Robots](https://www.youtube.com/watch?v=_liJnDf8a7k)**

Subscribe for more: https://www.youtube.com/@carrosshow9598 Other video's: These $100 Korean AI Drones Can Make You Fly: ...

📺 Carros Show

👁️ 59K • 👍 1K • 💬 127 • ⏱️ 9:36 • 5d ago

---

**[DON’T INVEST in Ultimate Molots until War Robots buffs them!](https://www.youtube.com/watch?v=SNDZb8IrHIw)**

War Robots Gameplay: Ultimate Molots on the Ravana - probably the worst of the ultimate weapons so far, I think. Do not invest in ...

📺 Manni-Gaming

👁️ 8K • 👍 427 • 💬 103 • ⏱️ 17:41 • 1d ago

---

**[Americans Can&#39;t Believe What China Built Now!](https://www.youtube.com/watch?v=krV1I2MCtd4)**

China is building robots faster than any country in the world and if you want to understand why robots are so important for China ...

📺 Cyrus Janssen

👁️ 262K • 👍 7K • 💬 1K • ⏱️ 11:41 • 6d ago

---

**[Tom Llamas meets humanoid robot &#39;Sprout.&#39; How this technology could soon become a family fixture](https://www.youtube.com/watch?v=XbAOMqkKLGU)**

Fauna Robotics is introducing Sprout, a humanoid robot designed as a friendly companion for homes and social spaces.

📺 NBC News

👁️ 124K • 👍 2K • 💬 429 • ⏱️ 12:16 • 4d ago

---

**[Honor’s First Humanoid Robot Unveils Its Dance Moves at MWC | What the Future](https://www.youtube.com/watch?v=NDph9DHvm60)**

Watch the official reveal of Honor's first humanoid service robot announced at MWC 2026. Read more at CNET.com First Steps?

📺 CNET

👁️ 40K • 👍 277 • 💬 24 • ⏱️ 1:27 • 1d ago

---

**[China’s Humanoid Robots Just Learned to FIGHT… The World Isn’t Ready](https://www.youtube.com/watch?v=auoP7Wk_7HA)**

China's humanoid robots have officially learned to fight, and the latest demonstrations show a level of power and precision the ...

📺 The AI Nexus

👁️ 4K • 👍 118 • 💬 25 • ⏱️ 24:08 • 5d ago

---

**[The Hard Truth About Mass Robot Deployment](https://www.youtube.com/watch?v=VTbd0_n9qQA)**

Tesla just shut down Model S and X lines to pivot toward Optimus production — but is this a real robotics breakthrough or a ...

📺 Dumb Money Live

👁️ 16K • 👍 426 • 💬 138 • ⏱️ 13:15 • 3d ago

---

**[Russia&#39;s Ameca Humanoid Robot #robotics #humanoidrobot #ai #airobot](https://www.youtube.com/watch?v=fhlVu7h6nH8)**

In Russia, the Perm Polytenic University is using an Ameca-like humanoid to help train engineering students in next-gen robotics ...

📺 Kalil 4.0

👁️ 888 • 👍 25 • ⏱️ 0:39 • 16h ago

---

---

*Generated by PeekDeck - A glance is all you need*
