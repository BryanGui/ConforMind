import { NavLink, Outlet } from "react-router-dom";

export default function AppLayout() {
  return (
    <div className="flex h-screen bg-[#f9f9fb] text-black">
      
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-gray-200 p-6 space-y-4">
        <h1 className="text-xl font-bold mb-8">ConforMind</h1>
        <nav className="flex flex-col gap-2 text-sm">
          <NavLink to="/Dashboard" className="text-gray-700 hover:text-black">Dashboard</NavLink>
          <NavLink to="/AIModels" className="text-gray-700 hover:text-black">Modèles IA</NavLink>
          <NavLink to="/Compliance" className="text-gray-700 hover:text-black">Conformité</NavLink>
          <NavLink to="/Reports" className="text-gray-700 hover:text-black">Rapports</NavLink>
          <NavLink to="/Settings" className="text-gray-700 hover:text-black">Paramètres</NavLink>
        </nav>
      </aside>

      {/* Main content */}
      <div className="flex-1 flex flex-col">
        
        {/* Header */}
        <header className="h-16 border-b border-gray-200 px-6 flex items-center justify-between bg-white">
          <div className="text-sm text-gray-600">Espace de travail : <strong>ConforTest</strong></div>
          <div className="text-sm text-gray-500">Utilisateur connecté</div>
        </header>

        {/* Page content */}
        <main className="flex-1 p-6 overflow-auto">
          <Outlet /> {/* Ici on injecte la page en cours */}
        </main>
      </div>
    </div>
  );
}
