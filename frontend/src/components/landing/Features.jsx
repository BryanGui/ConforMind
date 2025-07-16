export default function Features() {
  return (
    <section className="py-24 px-6 max-w-7xl mx-auto">
      <h2 className="text-3xl md:text-4xl font-semibold mb-12">Fonctionnalités clés</h2>
      <div className="grid md:grid-cols-3 gap-8">
        {[1, 2, 3].map((n) => (
          <div key={n} className="p-6 border border-white/10 rounded-xl">
            {/* TODO: Remplacer avec vraie feature */}
            <h3 className="text-xl font-medium mb-2">Titre fonctionnalité {n}</h3>
            <p className="text-sm text-white/70">Description de la fonctionnalité {n}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
