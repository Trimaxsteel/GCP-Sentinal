# GCP Sentinel: Cloud Security Posture Management (CSPM)

GCP Sentinel is an automated Cloud Security Posture Management (CSPM) tool designed to provide deep-visibility auditing for Google Cloud Platform environments. It interrogates cloud metadata in real-time to detect misconfigurations, IAM over-privileging, and storage leaks.

---

## 🚀 Key Features

- **Seven-Vector Risk Engine**: Proprietary logic to scan for IAM Leakage, Public GCS Buckets, Stale Keys, and Open Firewall Rules.
- **Real-Time API Interrogation**: Direct integration with Google Cloud SDK to pull live resource metadata.
- **Automated Remediation Playbooks**: One-click generation of Shell scripts to fix identified security gaps.
- **Dynamic Security Posture Scoring (SPS)**: A weighted algorithm that assesses overall project health.
- **Drift Detection**: Automated monitoring to identify when cloud settings deviate from secure benchmarks.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | React.js + TailwindCSS (SOC Dashboard Interface) |
| **Backend** | Python Flask (REST API & Cloud Interrogation Engine) |
| **Integration** | Google Cloud Client Libraries (Python) |
| **Deployment** | Docker & Docker-Compose (Multi-container orchestration) |

---

## 📂 Project Structure

```
GCP-Sentinel/
├── client/                 # React Frontend (Dashboard & Analytics)
│   ├── src/
│   │   ├── components/     # Risk Cards, Gauges, Score Widgets
│   │   └── hooks/          # useScanner, useProjects (API Logic)
├── server/                 # Flask Backend (The Brains)
│   ├── vectors/            # Security logic modules (IAM, Networking, Storage)
│   ├── playbooks/          # Remediation shell script templates
│   ├── app.py              # Central API Entry Point
│   └── audit_engine.py     # Main GCP SDK Interrogation Logic
├── docker-compose.yml      # Container Orchestration
└── .env                    # Environment Config (GCP Project ID, JWT Secret)
```

---

## ⚙️ How to Run

### 1. Setup GCP Credentials

Ensure you have a Service Account JSON key from your Google Cloud Console with Security Reviewer permissions. Place it in the `server/` directory.

### 2. Environment Configuration

Create a `.env` file in the root directory:

```
GCP_PROJECT_ID=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=./service-account-key.json
JWT_SECRET=your_dev_secret
```

### 3. Launch System

Run the entire stack using Docker:

```bash
docker-compose up -d --build
```

- **Dashboard**: http://localhost:3000
- **Backend API**: http://localhost:5000

---

## 📊 The Scoring Algorithm

The system evaluates security health based on the following weighted formula:

$$\text{SPS} = 100 - \sum(\text{Vulnerability} \times \text{Weight})$$

| Severity | Weight | Example Issue |
|----------|--------|---------------|
| Critical | 25 | Public GCS Bucket |
| High | 15 | IAM role with 'Owner' for allUsers |
| Medium | 5 | Stale API Key (>90 days) |

---

## 📜 Developer Note

This project was developed as a comprehensive 3rd-year engineering submission, covering the full lifecycle of cloud security auditing—from API interrogation to automated remediation. It demonstrates full-stack proficiency in cloud-native security development.

---

## 📝 License

This project is part of an academic capstone submission.
