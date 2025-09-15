import matplotlib.pyplot as plt
from ..utils import normalize_label

def theta_plot_fixed_k(df,k = 0,klabel = None, mark_point = None, save = None):
    """
    Plot the bifurcation diagram for a fixed value of k.
    
    Parameters:
        df (DataFrame): DataFrame containing the data to plot.
        k (float): Fixed value of k.
        klabel (str): Label for the k value.
        mark_point (tuple): Point to mark on the plot (x, y, z, label).
        save (str): Path to save the plot.
    
    Returns:
        None
    """
    assert k in df['k'].values, f"The value of k = {k} is not in the DataFrame."
    try:
        if klabel is None:
            klabel = str(k)
        filtered_df = df[df['k']==k]
        df_real = filtered_df[filtered_df['u_complex']==0]
        df_com = filtered_df[filtered_df['u_complex']!=0]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        ax1.scatter(df_real['b'], df_real['u_real'], color='red', s=1 , label='Real solutions')
        ax1.scatter(df_com['b'], df_com['u_real'], color='blue', s=1 , label='Real part (Complex solution)')
        if mark_point is not None:
            ax1.scatter(mark_point[0], mark_point[1], color='green', s=10 , label=mark_point[3])
        ax1.set_title('Real part plot')
        ax1.set_xlabel('$\\hat{\\beta}$')
        ax1.set_ylabel('Re($\\theta$)')
        ax1.axhline(0, color='black')
        ax1.axvline(0, color='black')
        ax1.grid(True)
        ax1.legend(loc='upper right')

        ax2.scatter(df_com['b'], df_com['u_complex'], color='blue', s=1 , label='Imaginary part Complex solutions')
        if mark_point is not None:
            ax2.scatter(mark_point[0], mark_point[2], color='green', s=10 , label=mark_point[3])
        ax2.set_title('Complex part plot')
        ax2.set_xlabel('$\\hat{\\beta}$')
        ax2.set_ylabel('Imag($u$)')
        ax2.axhline(0, color='black')
        ax2.axvline(0, color='black')
        ax2.grid(True)
        ax2.legend(loc='upper right')

        fig.suptitle(f'$\\theta$-Bifurcation Diagram for $\\hat{{k}} = {klabel}$', fontsize=16)

        plt.tight_layout()
        if save is not None:
            plt.savefig(save+f'/ThetaDiagram_KValue_{normalize_label(klabel)}_fixed2D.png')
        plt.show()
    except Exception as e:
        print(f'Plot Error: {e}')



def theta_plot_fixed_b(df,b = 0,blabel = None, mark_point = None , save = None):
    """
    Plot the bifurcation diagram for a fixed value of b.
    
    Parameters:
        df (DataFrame): DataFrame containing the data to plot.
        b (float): Fixed value of b.
        blabel (str): Label for the b value.
        mark_point (tuple): Point to mark on the plot (x, y, z, label).
        save (str): Path to save the plot.
        
    Returns:
        None
    """
    assert b in df['b'].values , f"The value of b = {b} is not in the DataFrame."
    try:
        if blabel is None:
            blabel = str(b)
        filtered_df = df[df['b']==b]
        df_real = filtered_df[filtered_df['u_complex']==0]
        df_com = filtered_df[filtered_df['u_complex']!=0]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        ax1.scatter(df_real['k'], df_real['u_real'], color='red', s=1 , label='Real solutions')
        ax1.scatter(df_com['k'], df_com['u_real'], color='blue', s=1 , label='Real part (Complex solution)')
        if mark_point is not None:
            ax1.scatter(mark_point[0], mark_point[1], color='green', s=10 , label=mark_point[3])
        ax1.set_title('Real part plot')
        ax1.set_xlabel('$\\hat{k}$')
        ax1.set_ylabel('Re($\\theta$)')
        ax1.axhline(0, color='black')
        ax1.axvline(0, color='black')
        ax1.grid(True)
        ax1.legend(loc='upper right')

        ax2.scatter(df_com['k'], df_com['u_complex'], color='blue', s=1 , label='Imaginary part Complex solutions')
        if mark_point is not None:
            ax2.scatter(mark_point[0], mark_point[2], color='green', s=10 , label=mark_point[3])
        ax2.set_title('Complex part plot')
        ax2.set_xlabel('$\\hat{k}$')
        ax2.set_ylabel('Imag($\\theta$)')
        ax2.axhline(0, color='black')
        ax2.axvline(0, color='black')
        ax2.grid(True)
        ax2.legend(loc='upper right')

        fig.suptitle(f'$\\theta$-Bifurcation Diagram for $\\hat{{\\beta}} = {blabel}$', fontsize=16)

        plt.tight_layout()
        if save is not None:
            plt.savefig(save+f'/ThetaDiagram_BetaValue_{normalize_label(blabel)}_fixed2D.png')
        plt.show()
    except Exception as e:
        print(f'Plot Error: {e}')

def theta_plot_kb_3d(df, id=None, mark_point_real=None, mark_point_complex=None, save=None, view_angle=(30, -60)):
    """
    Plot the bifurcation diagram in 3D for both real and complex parts of theta.
    
    Parameters:
    
        df (DataFrame): DataFrame containing the data to plot.
        id (str): Identifier for the plot.
        mark_point_real (tuple): Point to mark on the real part plot (x, y, z, label).
        mark_point_complex (tuple): Point to mark on the complex part plot (x, y, z, label).
        save (str): Path to save the plot.
        view_angle (tuple): View angle for the 3D plot (elev, azim).
        
    Returns:
        None
    """
    try:
        if id is None:
            id = "def"
        df_real = df[df['u_complex'] == 0]
        df_com = df[df['u_complex'] != 0]

        fig = plt.figure(figsize=(13, 7))

        ax1 = fig.add_subplot(121, projection='3d')
        ax2 = fig.add_subplot(122, projection='3d')

        # Real part plot
        ax1.scatter(df_real['k'], df_real['b'], df_real['u_real'], color='red', s=1, label='Real solutions')
        ax1.scatter(df_com['k'], df_com['b'], df_com['u_real'], color='blue', s=1, label='Real part (Complex solution)')
        if mark_point_real is not None:
            x, y, z, label = mark_point_real
            ax1.scatter(x, y, z, color='lightgreen', s=15, label=label)
        ax1.set_title('Real part plot')
        ax1.set_xlabel('$\\hat{k}$')
        ax1.set_ylabel('$\\hat{\\beta}$')
        ax1.set_zlabel('Re($\\theta$)', labelpad=10)
        ax1.zaxis.set_label_coords(-0.1, 0.5)
        ax1.grid(True)
        ax1.legend(loc='upper right')
        ax1.view_init(elev=view_angle[0], azim=view_angle[1])

        # Complex part plot
        ax2.scatter(df_com['k'], df_com['b'], df_com['u_complex'], color='blue', s=1, label='Imaginary part Complex solutions')
        if mark_point_complex is not None:
            x, y, z, label = mark_point_complex
            ax2.scatter(x, y, z, color='lightgreen', s=15, label=label)
        ax2.set_title('Complex part plot')
        ax2.set_xlabel('$\\hat{k}$')
        ax2.set_ylabel('$\\hat{\\beta}$')
        ax2.set_zlabel('Imag($\\theta$)', labelpad=10)
        ax2.zaxis.set_label_coords(-0.1, 0.5)
        ax2.grid(True)
        ax2.legend(loc='upper right')
        ax2.view_init(elev=view_angle[0], azim=view_angle[1])

        fig.suptitle(f'Bifurcation Diagram for $\\theta$ values', fontsize=16)

        plt.tight_layout()
        if save is not None:
            plt.savefig(save + f'/ThetaDiagram_KB_{normalize_label(id)}_fixed3D.png')
        plt.show()

    except Exception as e:
        print(f'Plot Error: {e}')