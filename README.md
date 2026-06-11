# 🎧 Time Travel Playlist Generator

This project automatically creates a Spotify playlist based on the songs that were on the Billboard charts on a specific date chosen by the user. After entering a date, the system identifies the corresponding Saturday, retrieves the most popular songs from that week, and adds them to a private Spotify playlist.

If a playlist for that date already exists, it is reused instead of creating a new one, ensuring organization and avoiding duplicates.

---

## ✨ Features

- Validation of the date entered by the user  
- Automatic calculation of the corresponding Saturday  
- Retrieval of the week’s most popular songs from Billboard  
- Search for tracks on Spotify based on title and year  
- Automatic creation of a private playlist named after the selected date  
- Reuse of the playlist if it already exists  
- Addition of all found songs directly into the playlist  

---

## 🎯 Purpose

Provide a simple and automated way to musically revisit any week between 2020 and 2026, creating personalized playlists that reflect the biggest hits of the time.

---

## 📌 Process Flow

1. The user selects a date  
2. The system validates the date and determines the corresponding Saturday  
3. The songs from that week are retrieved from Billboard  
4. Each song is searched on Spotify  
5. The corresponding playlist is created or reused  
6. All found songs are automatically added  

---

## 📚 Notes

- Only songs found on Spotify are added  
- The playlist is always private  
- The playlist name follows the format: **Top Songs for YYYY-MM-DD**  
