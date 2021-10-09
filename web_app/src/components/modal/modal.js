/**
 * Modal component
 *
 * a floating modal with a background overlay
 */
function Modal({
    handleHide= () => {},
    children=null,
    bgOverlay='bg-gray-500',
    bgOpacity='bg-opacity-75',
    bg='bg-white',
    z='z-10',
    ...props
    }) {
  return <div {...props} class={`fixed ${z} inset-0 overflow-y-auto`} aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
    <div class={`fixed inset-0 ${bgOverlay} ${bgOpacity} transition-opacity`} aria-hidden="true" onClick={handleHide}/>
    <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
    <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
      <div class={`${bg} px-4 pt-5 pb-4 sm:p-6 sm:pb-4`}>
        {children}
        </div>
    </div>
  </div>
</div>;
}

export default Modal;