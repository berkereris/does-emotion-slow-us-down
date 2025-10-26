#  Does Emotion Slow Us Down?  
### *A Reaction Time Study on Emotional Valence and Scene Categorization*

#### Authors  
Ridha Alrubaye, Alp Eren Akyüz, Muhammet Öztürk, Alperen Çağlar, Berker Eriş   
Department of Artificial Intelligence and Data Engineering  
Istanbul Technical University  

---

## Overview
This project investigates how **emotional valence** (positive, neutral, negative) affects **reaction time and accuracy** in a binary image classification task.  
Participants categorized indoor and outdoor scenes while their response speed was recorded.  
The experiment was conducted using **PsychoPy**, and all analyses were performed in **Python (Jupyter Notebook)** using statistical methods such as **ANOVA** and **Tukey’s HSD**.

---

## Research Question
> **Does the emotional valence of an image affect how quickly people can categorize it as indoor or outdoor?**

**Hypothesis:** Emotionally charged images (positive or negative) would elicit slower reaction times than neutral images.

---

## Experimental Design
- **Participants:** 75 university students (balanced by gender, mean age 22)  
- **Stimuli:** 180 labeled images with emotional valence (positive, neutral, negative) and environment (indoor/outdoor)  
- **Task:** Binary classification (“Indoor” vs. “Outdoor”)  
- **Procedure:** Reaction times and accuracy recorded via PsychoPy  
- **Data Processing:** Outlier removal, normalization, and statistical testing (ANOVA + Tukey’s HSD)

---

## Results Summary
| Metric | Main Effect | p-value | Notes |
|---------|--------------|---------|-------|
| Reaction Time | Emotional Class | 0.02 | Only Neutral vs. Positive contrast significant |
| Reaction Time | Scene Category | < 0.001 | Outdoor scenes faster |
| Accuracy | Scene Category | < 0.001 | Indoor scenes less accurate |
| Emotion × Scene | None | n.s. | No interaction effect |

- **Conclusion:** Emotional valence has a measurable but subtle effect on speed. Scene type has a stronger influence on both speed and accuracy.

---

## 🧾 References
- [PsychoPy Documentation](https://www.psychopy.org/)
- [Statsmodels ANOVA Reference](https://www.statsmodels.org/)
- Alrubaye, R., Akyüz, A.E., Öztürk, M., Çağlar, A., & Eriş, B. (2025). *Does Emotion Slow Us Down?* ISBCS Conference, Bahçeşehir University.

---

## ✨ Acknowledgements
Special thanks to **Didem Gökçay** and **Şeyma Takır** for their guidance and feedback during this study.
