export default function Header() {
  return (
    <header className="py-6 px-6 flex justify-between items-center border-b border-white/10">
      <div className="text-lg font-bold">ConforMind</div>
      <nav>
        {/* TODO: Ajouter navigation ou bouton "Se connecter" */}
        <button className="text-sm text-white/70 hover:text-white transition">Se connecter</button>
      </nav>
    </header>
  );
}

