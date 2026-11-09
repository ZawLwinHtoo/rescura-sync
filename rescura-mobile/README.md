# Rescura mobile reporting demo

An optional Expo SDK 57 client for submitting location reports to a Supabase `sos_alerts` table. It is separate from the FastAPI dashboard. A database insert does not confirm receipt by a dispatcher, and this app is not connected to emergency services.

## Run

Requires Node.js 22.13 or later, as specified by [Expo SDK 57](https://docs.expo.dev/versions/v57.0.0/).

```sh
npm ci
npm run web
```

A fresh clone opens without cloud credentials. Submission displays a configuration message and sends nothing until you configure a project.

## Optional cloud connection

Copy `.env.example` to `.env` and configure your own `EXPO_PUBLIC_SUPABASE_URL` and `EXPO_PUBLIC_SUPABASE_ANON_KEY`. Public Expo variables are bundled into the client; never put a Supabase service role key there.

The configured project needs a `sos_alerts` table accepting `location`, `latitude`, `longitude`, `affected_people`, `affected_count`, `urgent_need`, and `status`. Its row level security policies must explicitly allow the intended insert. No cloud schema or permissions are changed by this application.

The browser or device asks for location permission on submission. Affected people must be a positive integer. Network failures and rejected inserts remain errors; the form only resets after the configured database accepts the insert.

## Build check

```sh
npx expo export --platform web
```

A web export checks bundling, not physical device GPS or your cloud policies. Those require verification with the configured device and project.
