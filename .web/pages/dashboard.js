import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Heading, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Spacer, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Box sx={{"alignItems": "flex-start", "transition": "left 0.5s, width 0.5s", "position": "relative", "marginLeft": "10em", "marginRight": "10em"}}>
  <Box sx={{"fontFamily": "sans-serif", "backgroundColor": "#BA9EF6", "textAlign": "center", "marginTop": "20", "width": "100%", "alignItems": "flex-start", "borderRadius": "0.375rem", "padding": "0.5em"}}>
  <Heading sx={{"fontSize": "3em"}}>
  {`one line at a time`}
</Heading>
</Box>
  <VStack>
  <Spacer/>
  <Box sx={{"border": "3px solid #BA9EF6", "marginTop": "1em", "width": "100%", "alignItems": "flex-start", "borderRadius": "0.375rem", "padding": "0.5em"}}>
  <Heading sx={{"fontSize": "2em"}}>
  {`about`}
</Heading>
  <Text>
  {`information`}
</Text>
  <Button sx={{"href": "/", "borderRadius": "0.375rem", "backgroundColor": "#BA9EF6", "opacity": "0.6"}}>
  {`continue`}
</Button>
</Box>
</VStack>
  <Spacer/>
</Box>
  <NextHead>
  <title>
  {`Dashboard`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
  <meta content={`width=device-width, shrink-to-fit=no, initial-scale=1`} name={`viewport`}/>
</NextHead>
</Fragment>
  )
}