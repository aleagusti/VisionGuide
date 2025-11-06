# VisionGuide – User Flows (v0.1)

This document describes the initial user-facing workflows for VisionGuide.  
These flows define how the system behaves, when it communicates, and what information it delivers in common mobility scenarios for blind and low-vision users.

---

## 1. Sidewalk Navigation

**Goal:** Provide continuous, low-interference awareness of obstacles and safe path.

### Flow
1. The camera captures the user’s forward direction (phone-held or glasses-mounted).
2. The system detects:
   - poles  
   - bollards  
   - curb up/down  
   - sidewalk holes or uneven surfaces  
   - scaffolding  
3. If a hazard is detected within 2–3 meters:
   - **Short haptic feedback**
   - **Brief audio cue**, for example:  
     - “Step left”  
     - “Curb up”  
     - “Hole ahead”
4. Non-critical obstacles → haptic-only.
5. Uncertain detection → conservative cue (“Caution ahead”).

---

## 2. Street Crossing With Traffic Light

**Goal:** Safely determine when to cross at intersections with pedestrian lights.

### Flow
1. VisionGuide recognizes:
   - crosswalk pattern  
   - traffic light head  
   - pedestrian signal  
2. System announces:  
   - “Crosswalk ahead, 2 meters.”
3. It evaluates traffic-light state:
   - **Red** → “Red light. Wait.”  
   - **Green** → system evaluates approaching vehicles before allowing crossing.
4. If safe to cross:  
   - “Green. Cross now. Keep straight.”
5. If unsafe:  
   - “Green, but car approaching right. Wait.”

---

## 3. Street Crossing Without Traffic Light

**Goal:** Provide situational awareness in mid-block crossings and uncontrolled intersections.

### Flow
1. Road boundary detected.
2. System analyzes vehicle direction, speed, and distance.
3. Announces:
   - “Road ahead.”  
   - “Two cars left, far.”  
   - “One car right, close. Do not cross.”
4. Re-evaluates every 1–2 seconds.

---

## 4. Text Reading (Street Signs, Stores, Bus Stops)

**Goal:** Deliver essential text without overwhelming the user.

### Flow
1. User points the device or faces the direction of the sign.
2. VisionGuide localizes the sign and performs OCR.
3. Reads concise output:
   - “Street sign: San Martín 1200.”  
   - “Store: Pharmacy.”  
   - “Bus stop. Lines 60, 132.”
4. Optional extended read:
   - User taps device → “Read full text.”

---

## 5. Exploration Mode (“What’s around?”)

**Goal:** Provide a short scene summary on demand.

### Flow
1. User long-presses a button or gesture.  
2. VisionGuide generates a scene caption, for example:  
   - “A bakery on your left. Cars parked on the right. One person walking toward you.”
3. Prioritize relevant elements such as doors, stairs, vehicles, and moving objects.

---

## 6. Emergency / Hazard Mode

**Goal:** Trigger immediate reaction with minimal cognitive load.

### Flow
1. Hazard engine detects:
   - fast approaching vehicle  
   - sudden drop (e.g., stairs)  
   - bicycle approaching from behind  
2. Output hierarchy:
   - **Instant hazard tone**
   - **Urgent verbal cue**: “Stop!”  
   - Optional detail after hazard:  
     - “Car from left, very close.”

---

## 7. Indoor Navigation (Future Roadmap)

**Goal:** Assist users in finding rooms, elevators, exits, and navigating large indoor spaces.

### Flow
1. Detect corridor geometry.
2. Detect door labels and building signage.
3. Cues include:
   - “Elevator ahead.”  
   - “Door 304 on your left in 3 meters.”

---

## Next Steps

These user flows support:
- feature prioritization  
- ML pipeline design  
- UX consistency  
- demo scenarios  
- requirements for the initial PoC models  

Further workflow documents:
- **ENGINEERING_FLOW.md** (technical pipelines)
- **FEATURE_DEMOS.md** (storyboards and mockups)
