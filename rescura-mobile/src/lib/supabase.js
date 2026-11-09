import { createClient } from '@supabase/supabase-js';

const url = process.env.EXPO_PUBLIC_SUPABASE_URL;
const anonKey = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY;

// A fresh clone must never write reports into somebody else's cloud project.
export const supabase = url && anonKey ? createClient(url, anonKey) : null;
