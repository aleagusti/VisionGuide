VisionGuide  
AI-Assisted Perception and Navigation System

VisionGuide is an open-source + commercially licensable platform that provides
real-time environmental understanding, obstacle detection, and advanced
navigation assistance through computer vision and artificial intelligence.

Its primary goal is to empower blind and low-vision individuals with greater
autonomy and safety. Its broader vision extends to becoming a universal AI
copilot for human mobility—supporting pedestrians, cyclists, motorcyclists,
and drivers in preventing accidents through real-time situational awareness.

---

Mission

Build assisted perception systems that enable any person—regardless of
visual ability—to navigate the world with safety, autonomy, and confidence.

Vision

Create the global standard for intelligent visual assistance, turning AI
into an accessible copilot for everyone: from blind and low-vision users to
drivers, cyclists, and all forms of personal mobility.

---

Key Features (Current & Planned)

Phase 1 — Mobile App (MVP)
- Real-time object detection
- Obstacle alerts
- Street sign reading (OCR)
- Traffic light state detection
- Audio-based navigation cues
- Scene description on demand
- Cloud or on-device inference (configurable)

Phase 2 — Smart Glasses Integration
- Hands-free navigation
- Continuous awareness of surroundings
- Spatial audio guidance
- Multimodal perception (vision + audio + inertial sensors)
- Low-latency local inference

Phase 3 — 360° Vision Helmet (Extended Use Cases)
- Full panoramic perception
- Early-warning system for collisions
- Lane/traffic awareness for cyclists and motorcyclists
- Sports safety (mountain biking, skiing, etc.)
- Platform for future autonomous-mobility augmentation

---

Feature Evolution: Audio-Based Navigation Cues (Detailed Roadmap)

Phase A — Vision-Only Contextual Cues (MVP)
- No GPS required
- Real-time obstacle alerts
- Vehicle and pedestrian motion cues
- Path alignment feedback (“step left/right”, “curb ahead”)
- Safe/unsafe crossing analysis from camera input
- On-demand scene summaries
Purpose: early usability for blind users, works anywhere indoors/outdoors.

Phase B — GPS-Assisted Orientation
- Optional geolocation via smartphone or wearable
- Cardinal direction awareness
- Distance-based alerts
- Map alignment with visual detections
Purpose: adds macro-orientation without full navigation stack.

Phase C — Hybrid Navigation (Vision + GPS)
- Routing engine + real-time visual safety
- Dynamic rerouting when obstacles block the path
- Examples:
  - “Cross when safe; traffic is slowing down.”
  - “Turn left after the crosswalk.”
  - “Sidewalk blocked, rerouting.”
Purpose: full intelligent navigation for urban mobility.

Phase D — Autonomous-Level Assistance
- Predictive models for moving objects
- High-speed alerts for cyclists, motorcyclists, and sports use
- 360° perception with helmet
- Adaptive safety bubble
Purpose: early-stage accident-prevention system.

---

Why VisionGuide?
- Addresses accessibility gaps
- Provides real-time assistance beyond human vision
- Compatible with commodity hardware
- Extensible and open for research
- Dual-licensed for commercial integration

---

Architecture Overview (High-Level)

VisionGuide Core  
- Perception Engine
	-Object Detection 
	-Scene Segmentation
	-Traffic Light Recognition
	-OCR + Text Understanding
	-3D Spatial Awareness (planned)  
- Audio Guidance Engine  
	-Spatial Audio
	-Navigation Prompts
	-Danger Alerts
	-On-Demand Descriptions
- Device Layer 
	-Mobile
	-Glasses
	-Helmet
- API Layer
	-Local Interface API
	-Optional Cloud API
	-Third-Party Integrations

A full workflow document will be provided separately.

---

Roadmap

-Phase 1 — Mobile App (MVP - current work)  
	-Core perception models
	-Audio navigation interface
	-On-device vs cloud inference modes
	-Early user testing with visually impaired individuals

Phase 2 — Wearable Integration  
	-Smart-glasses prototype
	-Optimized inference pipeline
	-Battery/power management
	-Field testing in real mobility conditions

Phase 3 — VisionGuide Helmet (360) 
	-Multi-camera panoramic system
	-Full environment mapping
	-Ultra-low-latency warnings
	-Support for cyclists, motorcyclists, and sports safety

Phase 4 — Commercial Partnerships  
	-Accessibility organizations
	-Smart-glasses manufacturers
	-Mobility and safety tech companies

---

Subscription Model for Official App

While the VisionGuide source code is released under AGPL-3.0-or-later,
the **official VisionGuide application** (iOS/Android/desktop/firmware)
is a commercial product.

The official app includes:
- 7-day free trial
- paid subscription (monthly, quarterly, semi-annual, or annual)

Users who compile VisionGuide from source under AGPL-3.0 do NOT receive:
- access to the official backend
- cloud inference services
- hosted perception models
- hybrid navigation engine
- subscription system
- updates or support

Government accessibility programs may provide the app free through
institutional agreements, but such programs require a commercial license.
Self-hosting of backend components, navigation engines, or cloud inference services is prohibited unless licensed commercially.

---

Installation  
Setup instructions will be added as the system evolves.

Current repository includes:
Placeholder directories
License files
Contribution guidelines
Early-stage development notes

---

Contributing  
See CONTRIBUTING.txt

---

License  
VisionGuide is dual-licensed:

AGPL-3.0-or-later (open-source)

Commercial proprietary license for closed-source usage, hardware
integration, or any activity incompatible with AGPL obligations.

See:

LICENSE.txt

DUAL LISENCING.txt
---

Notice 
Third-party libraries retain their own licenses. 
See NOTICE.txt

---

Contact  
For commercial licensing, partnerships, or collaboration:
agustialejandro@gmail.com

---

Acknowledgements  
VisionGuide is built with the purpose of creating real-world impact in
accessibility, safety, and human mobility.
Thank you for supporting open innovation and assistive technology.

