# Slack Bot for Expense Management 🚀

A smart Slack-integrated bot powered by Generative AI (GenAI), PaddleOCR, and PostgreSQL to automate and streamline employee expense submission and approval workflows.

> Developed by Surya S in collaboration with **SAP Labs, Bengaluru** as part of a mini-project at **PSG Institute of Technology and Applied Research (June 2024)**.

---

## 📌 Features

- 🧾 **Receipt Processing**: Accepts receipt images from employees.
- 🔍 **PaddleOCR Integration**: Extracts text (amount, date, vendor) from receipt images with high accuracy.
- 🤖 **NER Model**: Enhances data extraction using custom-trained Named Entity Recognition.
- 📦 **PostgreSQL Storage**: Securely stores user inputs, receipt data, and timestamps.
- 📲 **Slack Integration**: Employees interact directly in Slack, receive status updates, and get notified on approvals.
- ✅ **Manager Approval Workflow**: Notifies designated approvers using interactive Slack messages (adaptive cards).
- 📊 **Audit Trail**: Easily retrievable records for reporting and audit.

---

## 🧠 Tech Stack

| Layer        | Technology Used                   |
|--------------|-----------------------------------|
| Bot Platform | Slack API                         |
| OCR          | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |
| NLP/NER      | DistilBERT (custom fine-tuned model) |
| Backend      | Python, JSON                      |
| Database     | PostgreSQL                        |
| Integration  | Slack Block Kit, Interactive Cards |

---

## 🧱 Architecture Overview

1. **Frontend (Slack)**  
   - Users submit expense details via Slack.
   - Managers receive interactive approval cards.

2. **OCR Pipeline**  
   - PaddleOCR extracts key data from uploaded receipt images.
   - Text is passed through a custom NER model for fine-grained parsing.

3. **Backend (Python Scripts)**  
   - Handles Slack events and logic.
   - Stores and retrieves expense data from PostgreSQL.

4. **PostgreSQL Database**  
   - Maintains user details, receipts, status logs, and timestamps.

5. **Notification System**  
   - Sends real-time Slack notifications to approvers and submitters.

---

## 🔄 Workflow

1. Employee submits an expense with receipt image.
2. OCR processes the image and extracts details.
3. NER refines extracted data.
4. Data is saved in PostgreSQL.
5. Slack sends an interactive approval message to the manager.
6. Manager approves/rejects directly in Slack.
7. Status is updated, and both manager and employee are notified.

---

## 📷 Screenshots

<img width="1156" height="522" alt="image" src="https://github.com/user-attachments/assets/a2b1cb51-cf18-4f64-ae27-4d149fad7c1e" />
<img width="1085" height="679" alt="image" src="https://github.com/user-attachments/assets/29195e0b-d2e4-44f2-8ef4-81868c0d73fa" />
<img width="1034" height="673" alt="image" src="https://github.com/user-attachments/assets/2122f0d6-b5ee-4997-af39-479073de6112" />


---

## 🧪 Validation & Testing

- ✅ Receipt recognition tested across various formats.
- ✅ Slack UI and block kit thoroughly validated.
- ✅ Integration tested for Slack ↔ OCR ↔ Database.
- ✅ Data persistence verified via PostgreSQL.

---

## 📈 Future Improvements

- 🤖 Enhance OCR to support **handwritten** and **multi-language** receipts.
- 💱 Add automatic **currency conversion**.
- 📚 Integrate with **accounting tools** (e.g., QuickBooks).
- 🌐 Add **language detection and translation**.
- 🔔 Provide advanced notifications and status tracking.

---

## 🧑‍💻 Developers

- Surya S - [GitHub](https://github.com/Surya-S-17)
- Swadhi K
- Ganga Raj R

> Mentored by **Srihari M** (SAP Labs) and **Dr. S. Lokesh** (PSG iTech)

---

## 📄 License

This project is for academic use only under the guidance of SAP Labs & PSG iTech. For enterprise use, please contact the authors.

---

## 📚 References

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Slack API Docs](https://api.slack.com/)
- [HuggingFace - DistilBERT](https://huggingface.co/transformers/model_doc/distilbert.html)
