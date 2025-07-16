export default function Footer() {
  return (
    <footer className="py-10 px-6 text-center text-sm text-white/40 border-t border-white/10">
      © {new Date().getFullYear()} ConforMind. Tous droits réservés.
    </footer>
  );
}