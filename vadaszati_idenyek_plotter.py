
import plotly.graph_objects as go

months = ["Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb"]

subspecies_colors = {                                           #3,4,5,6,7,8,9,A,B,C,1,2
    "ünő":          ["#8ba02c" if x else "#dddddd" for x in [0,0,1,1,1,1,1,1,1,1,1,1]],
    "borjú":        ["#8ba02c" if x else "#dddddd" for x in [1,1,0,0,0,0,1,1,1,1,1,1]],
    "tehén":        ["#c02828" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,1]],
    "csapos bika":  ["#a0472c" if x else "#dddddd" for x in [1,0,0,0,0,0,1,1,1,1,1,1]],
    "selejt bika":  ["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,1,1,1,0]],
    "érett bika":   ["#a0472c" if x else "#dddddd" for x in [0,0,0,0,0,0,1,1,0,0,0,0]],
}

fig = go.Figure()


for idx, (subspecies, colors) in enumerate(subspecies_colors.items()):
    fig.add_trace(go.Barpolar(
        r=[1]*12,
        theta=[15 + i*30 for i in range(12)],  # Offset by 15 degrees
        width=[30]*12,
        base=[idx]*12,
        marker_color=colors,
        marker_line_color="white",
        marker_line_width=1,
        opacity=1.0,
        name=subspecies,
        hoverinfo="none",
    ))
    # Add a label for each ring at angle 0 (top)
    fig.add_trace(go.Scatterpolar(
        r=[idx + 0.5],
        theta=[190],
        mode="text",
        text=[subspecies],
        textfont=dict(size=16, color="white", family="Arial Black"),
        showlegend=False,
        hoverinfo="none",
    ))


fig.update_layout(
    polar=dict(
        angularaxis=dict(
            tickmode="array",
            tickvals=[15 + i*30 for i in range(12)],  # Offset by 15 degrees
            ticktext=months,
            direction="clockwise"
        ),
        radialaxis=dict(visible=False, range=[0, 6]),  # Adjust range for hole size
        hole=0.4  # 0.4 = 40% of plot radius is empty
    ),
    showlegend=False,
    title="Gímszarvas vadászati idények",
    font=dict(size=16, color="black", family="Arial Black"),
)

fig.show()
