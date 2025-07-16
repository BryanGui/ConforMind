export default function CTASection() {
  return (
    <section className="py-24 px-6 bg-gradient-to-b from-white to-[#f9f9fb] text-black text-center">
      <div className="max-w-2xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-semibold mb-6">
          Prêt à cadrer vos IA ?
        </h2>
        <p className="text-base text-gray-700 mb-10">
          Créez un compte gratuit et gardez vos modèles alignés avec le AI Act.
        </p>
        <button className="inline-block px-6 py-3 rounded-xl bg-black text-white font-medium hover:bg-neutral-800 transition shadow-md">
          Créer un compte
        </button>
      </div>
    </section>
  );
}
