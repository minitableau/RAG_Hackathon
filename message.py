import pandas as pd
from datetime import datetime, timedelta


# Correction de l'erreur et complétion des descriptions et formats de date pour 15 événements
events_in_english_expanded = [
    {"event": "Climate Change Conference", "description": "An international gathering aiming to address the pressing issues of climate change through dialogue and innovation. Experts, activists, and policymakers from around the world will convene to share insights, propose solutions, and forge collaborative efforts. The conference will feature keynote speeches, workshops, and panel discussions, focusing on sustainable practices, renewable energy solutions, and global policy reforms.", "date": datetime.now() + timedelta(days=126)},
    {"event": "International Technology Innovation Fair", "description": "This fair is a premier event for showcasing cutting-edge technological advances across various sectors, including artificial intelligence, robotics, and biotechnology. Leading innovators, tech companies, and startups will present their latest products and services, aiming to bridge the gap between invention and application. The event includes product demonstrations, networking opportunities, and investor meetings.", "date": datetime.now() + timedelta(days=129)},
    {"event": "Charity Concert for Reforestation", "description": "A charity concert featuring renowned international artists, aimed at raising awareness and funds for global reforestation efforts. The event will combine live music performances with educational segments about the importance of trees for our ecosystem. All proceeds will go towards planting trees around the world, supporting biodiversity, and combating climate change.", "date": datetime.now() + timedelta(days=90)},
    {"event": "Medical Research Marathon", "description": "A marathon event organized to support medical research for rare diseases. Participants will run to raise funds and awareness for cutting-edge research projects. The marathon aims to bring together communities, healthcare professionals, and researchers in a collective effort to address challenging medical conditions.", "date": datetime.now() + timedelta(days=120)},
    {"event": "International Science Fiction Film Festival", "description": "Celebrating the imagination and creativity of science fiction cinema, this festival showcases both new and classic sci-fi films. It features screenings, Q&A sessions with filmmakers, and panel discussions on the genre's impact on culture and society.", "date": datetime.now() + timedelta(days=150)},
    {"event": "Global Entrepreneurship Summit", "description": "A platform for entrepreneurs worldwide to network, share ideas, and find investment opportunities. The summit will cover the latest trends in innovation and business growth, with workshops, pitch sessions, and keynote speeches.", "date": datetime.now() + timedelta(days=180)},
    {"event": "International Art Biennale", "description": "An exhibition showcasing contemporary art from around the world, including installations, paintings, and multimedia works. The Biennale serves as a gathering place for artists, collectors, and art enthusiasts to celebrate creativity and exchange ideas.", "date": datetime.now() + timedelta(days=210)},
    {"event": "World Literature Festival", "description": "A gathering of authors, poets, and literary scholars to discuss the impact of literature on society and culture. The festival will feature panels, readings, and book signings, allowing attendees to engage with the literary world.", "date": datetime.now() + timedelta(days=240)},
    {"event": "Global Health Conference", "description": "Healthcare professionals will discuss global health challenges, including pandemics, healthcare equity, and innovations in medical technology. The conference aims to promote collaboration and share best practices.", "date": datetime.now() + timedelta(days=270)},
    {"event": "International Education Expo", "description": "An event for educators, students, and institutions to explore advancements in educational technology, curriculum development, and global education trends.", "date": datetime.now() + timedelta(days=300)},
    {"event": "Sustainable Agriculture Symposium", "description": "Farmers, scientists, and industry experts will explore sustainable farming practices, the impact of climate change on agriculture, and innovations in food security.", "date": datetime.now() + timedelta(days=330)},
    {"event": "Renewable Energy Forum", "description": "A forum dedicated to discussing the transition to renewable energy sources, featuring case studies, technological advancements, and policy discussions.", "date": datetime.now() + timedelta(days=360)},
    {"event": "Global Water Resources Workshop", "description": "Experts will discuss water conservation strategies, the impact of climate change on water resources, and solutions for ensuring clean and accessible water worldwide.", "date": datetime.now() + timedelta(days=390)},
    {"event": "International Cybersecurity Conference", "description": "Cybersecurity professionals will address the latest threats, data protection strategies, and the importance of cybersecurity in the digital age.", "date": datetime.now() + timedelta(days=420)},
    {"event": "World Peace Forum", "description": "Leaders and activists will discuss strategies for conflict resolution, peacebuilding, and fostering global cooperation and understanding.", "date": datetime.now() + timedelta(days=450)}
]

# Conversion des dates en format DD/MM/YY
for e in events_in_english_expanded:
    e["date"] = e["date"].strftime("%d/%m/%y")

# Création d'un DataFrame
df_events_in_english_detailed = pd.DataFrame(events_in_english_expanded)

# Sauvegarde en CSV
filename_english = "future_events_detailed_en.csv"
df_events_in_english_detailed.to_csv(filename_english, index=False)

filename_english
