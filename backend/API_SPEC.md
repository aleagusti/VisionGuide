# VisionGuide Backend – API Spec (draft)

## Authentication
- POST /v1/auth/login
- POST /v1/auth/refresh

## Subscriptions
- GET  /v1/subscription/status
- POST /v1/subscription/activate

## Perception (model proxy)
- POST /v1/perception/detect
- POST /v1/perception/scene

## Navigation (hybrid)
- POST /v1/navigation/route
- POST /v1/navigation/hazard