from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
	
        A = self.addSwitch( 's1' )
        B = self.addSwitch( 's2' )
	C = self.addSwitch( 's3' )
	D = self.addSwitch( 's4' )
	E = self.addSwitch( 's5' )

        # Add links
        self.addLink( Host1, D, 1, 1  )
        self.addLink( Host2,E, 1, 1 )

	self.addLink( A,D, 1, 2 )
	self.addLink( A,E, 2, 2 )
	self.addLink( B,D, 1, 3 )
	self.addLink( B,E, 2, 3 )
	self.addLink( C,D, 1, 4 )
        self.addLink( C,E, 2, 4 )


topos = { 'mytopo': ( lambda: MyTopo() ) }

