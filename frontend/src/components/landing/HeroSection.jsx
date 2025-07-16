import "@fontsource/inter"; // 👈 à ajouter UNE SEULE FOIS au début de ton projet (ex: dans main.jsx ou index.css si pas déjà fait)

export default function HeroSection() {
  return (
    <section className="relative w-full py-24 text-black overflow-hidden bg-[#f9f9fb] font-inter">
      {/* Background radial blur */}
      <div className="absolute inset-0 pointer-events-none">
        <div className="absolute top-[-10%] left-[-20%] w-[600px] h-[600px] bg-purple-300 opacity-30 blur-3xl rounded-full" />
        <div className="absolute bottom-[-20%] right-[-10%] w-[500px] h-[500px] bg-blue-300 opacity-30 blur-3xl rounded-full" />
      </div>

      {/* Main content */}
      <div className="relative max-w-7xl mx-auto px-6 md:px-12 grid grid-cols-1 md:grid-cols-2 gap-16 items-center z-10">
        
        {/* LEFT */}
        <div>
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight leading-tight mb-6 bg-clip-text text-transparent bg-gradient-to-tr from-black to-gray-700">
            Conformité IA. Simplifiée.
          </h1>
          <p className="text-base text-gray-700 mb-8">
            Centralisez vos démarches, suivez vos modèles, restez conforme. Un point d’entrée unique pour votre mise en conformité IA Act.
          </p>
          <button className="inline-block px-6 py-3 bg-black text-white rounded-xl font-medium hover:bg-neutral-800 transition shadow-md">
            Commencer maintenant
          </button>
        </div>

        {/* RIGHT – NE PAS TOUCHER LE MOCKUP 😅 */}
        <div className="w-full h-[300px] rounded-2xl border border-dashed border-gray-300 flex items-center justify-center text-gray-400 text-sm bg-white">
          Ici viendra un mockup produit
        </div>
      </div>
    </section>
  );
}
