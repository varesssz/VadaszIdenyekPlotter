import plotly.graph_objects as go
from vadaszati_idenyek import ideny

# Iterate over every species
for select in range(9):
    # Import seasons from a different file
    (months, species, subspecies_colors, strip_size) = ideny(select)

    # Create a figure and update layout
    fig = go.Figure()
    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=50),
        polar=dict(
            angularaxis=dict(
                tickmode="array",
                tickvals=[15 + i*30 for i in range(12)],  # positions of the twelve months' ticks
                ticktext=months,
                direction="clockwise"
            ),
            radialaxis=dict(visible=False, range=[0, len(subspecies_colors)]),  # Adjust range for number of subspecies
            hole=1-strip_size,  # 100% - (strip size) of plot radius is empty
        ),
        font=dict(
            family='Arial',
            size=18,
            color='black',
        ),
        showlegend=False,
    )
    
    # Add the species' name in the middle of the polar plot
    fig.add_annotation(
        text=species,
        x=0.5,
        y=0.5,
        font=dict(size=30, color="black"),
        showarrow=False,
        xref="paper",
        yref="paper"
    )

    # Interate over the subspecies and the season data (colors)
    for idx, (subspecies, colors) in enumerate(subspecies_colors.items()):
        # Set default strip segments
        thetas = [15 + i*30 for i in range(12)]  # positions of the twelve 30° wide segments (offset by 15°)
        widths = [30]*12  # twelve 30° wide segments
        
        # Bisect a segment if a subspecie's season starts in the middle of the month
        if colors[1] is not None:
            ind = months.index(colors[1])  # find the segment
            thetas.insert(ind+1, 15+ind*30+7.5)  # insert a new segment
            thetas[ind] = thetas[ind]-7.5  # make the original segment thiner
            widths.insert(ind+1, 15)  # insert a new segment
            widths[ind] = 15  # make the original segment thiner
        
        # Add a trace to the plot
        fig.add_trace(go.Barpolar(
            r=[1]*len(thetas),
            theta=thetas,
            width=widths,
            base=[idx]*len(thetas),
            marker_color=colors[0],
            marker_line_color="white",
            marker_line_width=1,
            opacity=1.0,
            name=subspecies,
            hoverinfo="none",
        ))
        
        # Add a label for each ring at the bottom (180°)
        fig.add_trace(go.Scatterpolar(
            r=[idx + 0.5],
            theta=[180],
            mode="text",
            text=[subspecies],
            textposition="middle center",
            textfont=dict(size=18, color="#ffffff", shadow="auto", family="Arial"),
            showlegend=False,
            hoverinfo="none",
        ))

    # Show figure on browser
    fig.show()
