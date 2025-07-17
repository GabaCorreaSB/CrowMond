# 🛡️ CrowdMon: Grafana Edition

> One-command, plug-and-play visualization for CrowdSec alerts using Grafana & PostgreSQL  
> Built by Gabriel Correa dos Santos Barbosa — fully open-source, lab-ready.

---

### 🔍 What Is This?

CrowdMon is a **drop-in stack** that gives you real-time dashboards for **CrowdSec** using:

- 🛡️ CrowdSec for log-based intrusion detection
- 📦 A Python exporter to collect alerts
- 🗃️ PostgreSQL to store structured event data
- 📊 Grafana to visualize and explore security trends

It's lightweight, containerized, and lab-tested — made for learners, hackers, and engineers who want clarity, not complexity.

---

### 🚀 Install It Like Oh My Zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/GabaCorreaSB/crowdmon-grafana/main/install.sh)"
```

This will:
- Clone the repo into `~/.crowdmon-grafana`
- Start CrowdSec, Grafana, PostgreSQL, and the exporter
- Feed alerts into your dashboards automatically

---

### 🔧 What's Included

| Service       | Port         | Role                                  |
|---------------|--------------|----------------------------------------|
| CrowdSec      | `8080`       | Log monitoring & alerting engine       |
| PostgreSQL    | internal     | Alert storage (used by Grafana)        |
| Exporter      | internal     | Feeds CrowdSec alerts to the database  |
| Grafana       | `3000`       | Visual dashboards for everything       |

---

### 🎯 Why Use This?

- ✅ One-command setup
- ✅ Secure — no exposed `.db` files
- ✅ Fully open source
- ✅ Great for home labs, CTF prep, or real use

---

### ✨ Sample Dashboards to Build

- 🔥 Top attackers by IP
- ⏱️ Alerts per hour/day/week
- 🌍 Attack origin map (with optional IP geolocation)
- 📊 Scenario frequency (ssh bruteforce, port scans, etc.)

---

### 🧠 Ideal For

- Students building **cybersecurity labs**
- Engineers running **local SIEMs**
- Red teamers doing **recon simulation**
- Blue teamers doing **alert visualization**

---

### 🛠️ Folder Structure

```
crowdmon-grafana/
├── install.sh         # Oh-My-Zsh style installer
├── setup.sh           # Runs the stack
├── docker-compose.yml
└── exporter/
    ├── exporter.py
    └── Dockerfile
```

---

### 📜 License

MIT License  
© 2025 Gabriel Correa dos Santos Barbosa  
Use it, share it, improve it. That’s what it’s for.

---

### 🙌 Contributions Welcome

Spotted a bug? Got a dashboard idea? Submit a PR or open an issue. Let's make CrowdMon even better.

